"""
Codeforces Round 

Problem B. Simple Game

@author yamaton
@date 2015-08-13
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(n, m):
    if n == 1:
        return 1
    if m <= n // 2:
        return m + 1
    else:
        return m - 1


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    result = solve(n, m)
    print(result)


def __starting_point():
    main()


__starting_point()
