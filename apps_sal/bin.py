from __future__ import annotations
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


def print_in_upperline(*s, upper: int = 0) -> None:
    if len(s) > 0:
        to_upper_line = '\033[F' * upper
        print(to_upper_line + s[0], *s[1:])
        if upper >= 1:
            print('\n' * (upper - 1), end='', flush=True)


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
    parser.add_argument('-m', '--mode', default='eval', choices=['save', 'eval'], help='mode (default=eval)')
    parser.add_argument('-s', '--set', default='test', choices=['train', 'test'], help='set to use (default=test)')
    parser.add_argument('-t', '--target', default='apps.jsonl', type=str, metavar='<*.jsonl|*.json>', help='file that has program data (apps.jsonl)')
    parser.add_argument('-to', '--timeout', default=None, type=int, metavar='<int>', help='time budget for each program in eval mode (default=None)')
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
        for key, programs in target.items():
            print(f'Problem: {key}\n')
            problem = dataset.query(key)
            printed_lines = 1
            for i, program in enumerate(programs):
                print_in_upperline(f' Status: evaluating candidate {i + 1}', upper=printed_lines)
                with NewlineMonitor() as monitor:
                    score = problem.score(program, timeout=args.timeout)
                printed_lines += monitor.newlines
                if score == 1.0:
                    result[key] = 'solved'
                    break
            else:
                result[key] = 'failed'
            print_in_upperline(f' Status: {result[key]}                        ', upper=printed_lines)
            print()

        total = len(target)
        solved = sum((1 for r in result if r == 'solved'))
        print(f'Solve rate: {solved} / {total} ({solved / total * 100:.2f}%)')
