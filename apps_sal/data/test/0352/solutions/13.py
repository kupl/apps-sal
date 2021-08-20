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


def I():
    return int(input())


def LIST(n, m=None):
    return [0] * n if m is None else [[0] * m for i in range(n)]


def ELIST(n):
    return [[] for i in range(n)]


def MI(n=None, m=None):
    if n is None:
        (n, m) = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = VI()
    return arr


def MS(n=None, m=None):
    if n is None:
        (n, m) = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = input()
    return arr


def MIT(n=None, m=None):
    if n is None:
        (n, m) = VI()
    a = MI(n, m)
    arr = LIST(m, n)
    for (i, l) in enumerate(a):
        for (j, x) in enumerate(l):
            arr[j][i] = x
    return arr


def run(n, x, l, r):
    s = 0
    curr = 1
    for i in range(n):
        skip = (l[i] - curr) // x
        s += r[i] - curr - skip * x + 1
        curr = r[i] + 1
    print(s)


def main(info=0):
    n = I()
    (an, ax) = VI()
    (bn, bx) = VI()
    (cn, cx) = VI()
    m = [an, bn, cn]
    if sum(m) < n and ax > an:
        m[0] += min(ax - an, n - sum(m))
    if sum(m) < n and bx > bn:
        m[1] += min(bx - bn, n - sum(m))
    if sum(m) < n and cx > cn:
        m[2] += min(cx - cn, n - sum(m))
    print(m[0], m[1], m[2])


def __starting_point():
    main()


__starting_point()
