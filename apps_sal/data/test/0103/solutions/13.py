#!/usr/bin/env python3
from typing import Dict, List, Tuple


def input_lst() -> List[int]:
    return [int(x) for x in input().split()]


def print_out(res: List[int]):
    print(' '.join([str(x) for x in res]))


def main():
    n, = (int(x) for x in input().split())
    a = input_lst()

    l = 0
    l_max = 0
    if a[0] == 1:
        l += 1

    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            l += 1
        else:
            if l > 0:
                l_max = max(l, l_max)
                l = 0

    if l > 0:
        if a[-1] == 1000:
            l += 1
        l_max = max(l, l_max)

    print(max(l_max - 1, 0))


def __starting_point():
    main()


__starting_point()
