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
    parser.add_argument('-s', '--set', default='test', choices=['train', 'test'], help='set to use')
    parser.add_argument('-t', '--target', default=None, type=str, metavar='<*.jsonl|*.json>', help='generated programs')
    args = parser.parse_args(argv)

    dataset_loader = {
        'train': load_train_dataset,
        'test': load_test_dataset
    }[args.set]
    dataset = dataset_loader()
