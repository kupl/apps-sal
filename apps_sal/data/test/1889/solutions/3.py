import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict


def VI():
    return list(map(int, input().split()))


def get_score(x):
    b = 0
    best = 0
    running = 0
    for (i, v) in enumerate(x):
        if v == 1:
            if running:
                b += 1
            else:
                b = 1
            running = 1
        else:
            if running:
                if b > best:
                    best = b
            running = 0
    if b > best:
        best = b
    return best


def main_input(info=0):
    (n, m, q) = VI()
    g = list(range(n))
    sc = list(range(n))
    for i in range(n):
        g[i] = VI()
        sc[i] = get_score(g[i])
    r = list(range(q))
    for k in range(q):
        (i, j) = VI()
        (i, j) = (i - 1, j - 1)
        g[i][j] = 1 - g[i][j]
        sc[i] = get_score(g[i])
        print(max(sc))


def __starting_point():
    main_input()


__starting_point()
