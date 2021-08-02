#!/usr/bin/env python3
from typing import Dict, List, Tuple


def input_lst() -> List[int]:
    return [int(x) for x in input().split()]


def print_out(res: List[int]):
    print(' '.join([str(x) for x in res]))


def main():

    n, = (int(x) for x in input().split())
    #a = input_lst()
    s = input()
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            print(s[:i] + s[i + 1:])
            return
    print(s[:-1])


def __starting_point():
    main()


__starting_point()
