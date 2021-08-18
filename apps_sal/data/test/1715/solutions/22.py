import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    a, b, q = ns()
    s = [ni() for _ in range(a)]
    t = [ni() for _ in range(b)]

    def disLR(a, idx):
        small = a[max(0, idx - 1)]
        large = a[min(len(a) - 1, idx)]
        return [small, large]

    for _ in range(q):
        ans = INF

        x = ni()

        idxs = bisect.bisect_left(s, x)
        a1 = disLR(s, idxs)

        idxt = bisect.bisect_left(t, x)
        a2 = disLR(t, idxt)

        for ta1 in a1:
            for ta2 in a2:
                tmp1 = abs(x - ta1) + abs(ta2 - ta1)
                tmp2 = abs(x - ta2) + abs(ta1 - ta2)
                ans = min(ans, tmp1, tmp2)

        print(ans)


def __starting_point():
    main()


__starting_point()
