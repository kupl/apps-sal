import collections
import itertools
import functools
import math


def solve():
    n = int(input())
    p = list(map(int, input().split()))
    pos = [(p, i) for (i, p) in enumerate(p)]
    pos.sort()
    longest = 1
    seq = 1
    for i in range(1, n):
        if pos[i - 1][1] < pos[i][1]:
            seq += 1
        else:
            seq = 1
        longest = max(longest, seq)
    return n - longest


def __starting_point():
    print(solve())


__starting_point()
