"""
Codeforces Educational Round

Problem 598 B Queries on a String

@author yamaton
@date 2015-11-12
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def cycle_shift(s, k):
    n = len(s)
    k %= n
    return s[(n - k):] + s[:(n - k)]


def solve(triples, s, m):
    for (l, r, k) in triples:
        s = s[:l - 1] + cycle_shift(s[l - 1:r], k) + s[r:]
    return s


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    s = input()
    m = int(input())
    triples = [tuple(int(c) for c in input().strip().split()) for _ in range(m)]

    result = solve(triples, s, m)
    print(result)


def __starting_point():
    main()


__starting_point()
