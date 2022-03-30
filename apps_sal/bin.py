from __future__ import annotations
from collections import defaultdict
from io import StringIO
from typing import Dict
from typing import List
from typing import Union
from pathlib import Path
import argparse
import json
import sys

from apps_sal import load_train_dataset
from apps_sal import load_test_dataset
from apps_sal.logger import get_logger
from apps_sal.metric import Metric
from apps_sal.metric import PassAtK
from apps_sal.metric import StrictAccuracy
from apps_sal.metric import TestcaseAccuracy


def load_jsonl(path: Union[str, Path]) -> Dict[str, List[str]]:
    path = Path(path)
    data = {}
    text = path.read_text('utf-8')
    text = text.splitlines()
    for line in text:
        line = json.loads(line)
        data[line['id']] = line['codes']
    return data


def load_json(path: Union[str, Path]) -> Dict[str, List[str]]:
    path = Path(path)
    return json.loads(path.read_text('utf-8'))


def print_in_upperline(*s, upper: int = 0, filemode: bool = False) -> None:
    if len(s) > 0:
        to_upper_line = ''
        if not filemode:
            to_upper_line = to_upper_line + '\033[F' * upper
        print(to_upper_line + s[0], *s[1:])
        if not filemode:
            if upper >= 1:
                print('\n' * (upper - 1), end='', flush=True)


def make_metric(metrics: List[str], ks: List[int]) -> List[Metric]:
    metric_objects = []
    for metric in metrics:
        if metric == 'pass@k':
            for k in ks:
                metric_objects.append(PassAtK(k))
        else:
            if metric == 'strict':
                metric_objects.append(StrictAccuracy())
            elif metric == 'testcase':
                metric_objects.append(TestcaseAccuracy())
    return metric_objects


class NewlineMonitor:

    def __init__(self):
        # self.newlines: int = 0
        self.stream: StringIO = StringIO()
        self.stream.close = lambda _: 1
        self.out: Union[None, str] = None

    def __enter__(self) -> NewlineMonitor:
        sys.stdout = self.stream
        sys.stderr = self.stream
        return self

    def __exit__(self, *_) -> None:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.out = self.stream.getvalue()
        print(self.out, end='', flush=True)

    @property
    def newlines(self) -> int:
        return self.out.count('\n')


def main(argv=None):

    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='eval', choices=['save', 'eval'],
                        help='mode (default=eval)')
    parser.add_argument('-s', '--set', default='test', choices=['train', 'test'],
                        help='set to use (default=test)')
    parser.add_argument('-t', '--target', default='apps.jsonl', type=str,
                        metavar='<*.jsonl|*.json>',
                        help='file that has program data (apps.jsonl)')
    parser.add_argument('-to', '--timeout', default=None, type=int, metavar='<int>',
                        help='time budget for each program in eval mode (default=None)')
    parser.add_argument('--start', default=0, type=int, metavar='<int>',
                        help='start point of index range (default=0)')
    parser.add_argument('--end', default=5000, type=int, metavar='<int>',
                        help='end pint of index range (default=5000)')
    parser.add_argument('--metric', default=['strict'], nargs='+',
                        choices=['strict', 'testcase', 'pass@k'],
                        help='metric (default=strict)')
    parser.add_argument('--pass-at-k', default=[1], nargs='+', metavar='<int>', type=int,
                        help='k for pass@k (default=1)')
    parser.add_argument('--filemode', action='store_true', help='print in filemode')
    args = parser.parse_args(argv)

    dataset_loader = {
        'train': load_train_dataset,
        'test': load_test_dataset
    }[args.set]
    dataset = dataset_loader()

    if args.mode == 'save':
        pass

    # if args.mode == 'eval'
    else:
        target = Path(args.target)
        target_loader = {
            '.jsonl': load_jsonl,
            '.json': load_json
        }[target.suffix]
        target = target_loader(target)

        result = defaultdict(list)
        evaluated = 0
        for key, programs in target.items():
            if int(key) < args.start or int(key) >= args.end:
                continue
            print(f'Problem: {key}')
            evaluated += 1
            problem = dataset.query(key)
            if problem is None:
                get_logger().warning('No problem is found. Skipped. Index: %s', key)
                print()
                continue
            if not args.filemode:
                print()
            printed_lines = 1
            for i, program in enumerate(programs):
                print_in_upperline(f' Status: evaluating candidate {i + 1}', upper=printed_lines, filemode=args.filemode)
                with NewlineMonitor() as monitor:
                    score = problem.score(program, timeout=args.timeout)
                printed_lines += monitor.newlines
                result[key].append(score)
            print_in_upperline(f' Status: Done   Max score: {max(result[key]) if len(result[key]) > 0 else 0.0:.2f}                     ', upper=printed_lines, filemode=args.filemode)
            print()

        metrics = make_metric(args.metric, args.pass_at_k)
        for metric in metrics:
            metric.print_report(result, dataset)
