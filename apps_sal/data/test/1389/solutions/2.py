import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import copy
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque


def VI():
    return list(map(int, input().split()))


def LIST(n, m=None):
    return [0] * n if m is None else [[0] * m for i in range(n)]


def run2(n, m, f):
    c = LIST(n, m)
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if f[i][j] != c[i][j]:
                ans += 1
                for k in range(i + 1):
                    for l in range(j + 1):
                        c[k][l] += f[i][j] - c[i][j]
    print(ans)


def main2(info=0):
    (n, m) = VI()
    f = list(range(n))
    for i in range(n):
        f[i] = [1 if x == 'W' else -1 for x in input()]
    run2(n, m, f)


def __starting_point():
    main2()


__starting_point()
