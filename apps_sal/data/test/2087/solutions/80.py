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

# _INPUT = """# paste here...
# """
# sys.stdin = io.StringIO(_INPUT)

MOD = 998244353

# def solve(A: int, B: int, C: int) -> int:


def solve(A, B, C):
    pass  # TODO: edit here


def main():
    A, B, C = list(map(int, input().split()))
    a = (A * (A + 1) // 2) * (B * (B + 1) // 2) * (C * (C + 1) // 2)
    print((a % MOD))


def __starting_point():
    main()


__starting_point()
