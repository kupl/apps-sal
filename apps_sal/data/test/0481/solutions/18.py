"""
Codeforces Round #319 (Div. 2)

Problem 577 A. Multiplication Table

@author yamaton
@date 2015-09-10
"""
import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(n, x):
    sqx = int(math.sqrt(x))
    lim = min(sqx, n)
    count = sum((2 for i in range(1, lim + 1) if x % i == 0 and x // i <= n))
    if sqx * sqx == x and sqx <= n:
        count -= 1
    return count


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, x] = [int(i) for i in input().strip().split()]
    result = solve(n, x)
    print(result)


def __starting_point():
    main()


__starting_point()
