"""
Codeforces Testing Round #12

Problem 597B. Restaurant

@author yamaton
@date 2015-11-11
"""
import math
import operator
import random
import sys
import functools
import collections


def solve(pairs):
    pairs.sort(key=operator.itemgetter(1))
    progress = -1
    cnt = 0
    for (s, f) in pairs:
        if progress < s:
            progress = f
            cnt += 1
    return cnt


def solve0(pairs):
    pairs.sort()
    d = collections.defaultdict(int)
    maxval = 0
    for (s, f) in pairs:
        d[f] = 1 + max((d[k] for k in d.keys() if k < s), default=0)
        maxval = max(maxval, d[f])
    return maxval


def p(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    pairs = [tuple((int(i) for i in input().strip().split())) for _ in range(n)]
    result = solve(pairs)
    print(result)


def __starting_point():
    main()


__starting_point()
