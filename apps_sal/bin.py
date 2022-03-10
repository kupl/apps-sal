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


def main(argv=None):

    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='eval', choices=['save', 'eval'], help='mode (default=eval)')
    parser.add_argument('-s', '--set', default='test', choices=['train', 'test'], help='set to use (default=test)')
    parser.add_argument('-t', '--target', default='apps.jsonl', type=str, metavar='<*.jsonl|*.json>', help='file that has program data (apps.jsonl)')
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
            print(f'Problem: {key}')
            problem = dataset.query(key)
            for i, program in enumerate(programs):
                print(f'\rStatus: evaluating candidate {i + 1}', end='', flush=True)
                score = problem.score(program)
                if score == 1.0:
                    result[key] = 'solved'
                    break
            else:
                result[key] = 'failed'
            print(f'\rStatus: {result[key]}                        ')
            print()

        total = len(target)
        solved = sum((1 for r in result if r == 'solved'))
        print(f'Solve rate: {solved} / {total} ({solved / total * 100:.2f}%)')
