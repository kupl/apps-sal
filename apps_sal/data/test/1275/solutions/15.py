# region Header
#!/usr/bin/env python3
# from typing import *

import sys
import io
import math
import collections
import decimal
import itertools
from queue import PriorityQueue
import bisect


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)
# endregion

# _INPUT = """2 1
# """
# sys.stdin = io.StringIO(_INPUT)


# def solve(N: int, K: int) -> int:
def solve(N, K):
    s = 0
    for Y in range(2, 2 * N + 1):
        X = Y + K
        if 2 <= X <= 2 * N:
            a_min = max(X - N, 1)
            a_max = min(X - 1, N)
            c_min = max(Y - N, 1)
            c_max = min(Y - 1, N)
            if a_min <= a_max or c_min <= c_max:
                s += (a_max - a_min + 1) * (c_max - c_min + 1)
    return s


def main():
    N, K = list(map(int, input().split()))
    a = solve(N, K)
    print(a)


def __starting_point():
    main()


__starting_point()
