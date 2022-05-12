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
    parser.add_argument('--end', default=4999, type=int, metavar='<int>',
                        help='end pint of index range (default=4999)')
    parser.add_argument('--metric', default=['strict'], nargs='+',
                        choices=['strict', 'testcase', 'pass@k'],
                        help='metric (default=strict)')
    parser.add_argument('--pass-at-k', default=[1], nargs='+', metavar='<int>', type=int,
                        help='k for pass@k (default=1)')
    parser.add_argument('--processes', default=1, type=int, metavar='<int>',
                        help='number of processes to use (default=1)')
    parser.add_argument('--score-json', default=None, metavar='<json>', type=str,
                        help='json file to store evaluated scores')
    parser.add_argument('--table', default=None, metavar='<txt>', type=str,
                        help='txt file to save metric reports')
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

        result = {}
        start = max(0, args.start)
        end = min(4999, args.end)
        for key in range(start, end + 1):
            print(f'Problem: {key}')
            problem = dataset.query(key)
            if problem is None:
                get_logger().warning('No problem is found. Skipped. Key: %s', key)
                print()
                continue
            result[key] = []
            try:
                programs = target[str(key)]
            except KeyError:
                get_logger().warning('No submission is found. This problem is treated as wrong. Key: %s', key)
                continue
            for i, program in enumerate(programs):
                print(f' Status: evaluating candidate {i + 1}')
                score = problem.score(program, timeout=args.timeout, processes=args.processes)
                result[key].append(score)
            print(f' Status: Done   Max score: {max(result[key]) if len(result[key]) > 0 else 0.0:.2f}')
            print()

        metrics = make_metric(args.metric, args.pass_at_k)
        if args.table is not None:
            table_file = Path(args.table)
            with table_file.open('w', encoding='utf8') as f:
                for metric in metrics:
                    metric.print_report(result, dataset, file=f)
        else:
            for metric in metrics:
                metric.print_report(result, dataset)

        if args.score_json is not None:
            score_json = Path(args.score_json)
            score_json.write_text(json.dumps(result, indent=4), encoding='utf-8')
