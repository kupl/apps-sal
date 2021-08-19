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

# Guide:
#   1. construct complex data types while reading (e.g. graph adj list)
#   2. avoid any non-necessary time/memory usage
#   3. avoid templates and write more from scratch
#   4. switch to "flat" implementations


def VI(): return list(map(int, input().split()))
def I(): return int(input())
def LIST(n, m=None): return [0] * n if m is None else [[0] * m for i in range(n)]
def ELIST(n): return [[] for i in range(n)]


def MI(n=None, m=None):  # input matrix of integers
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = VI()
    return arr


def MS(n=None, m=None):  # input matrix of strings
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = input()
    return arr


def MIT(n=None, m=None):  # input transposed matrix/array of integers
    if n is None:
        n, m = VI()
    a = MI(n, m)
    arr = LIST(m, n)
    for i, l in enumerate(a):
        for j, x in enumerate(l):
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
    a = VI()

    d = {}
    for i, x in enumerate(a):
        if x in d:
            (l, r, num) = d[x]
            d[x] = (l, i, num + 1)
        else:
            d[x] = (i, i, 1)

    best = (0, 1e7)
    bestv = None
    for k, v in list(d.items()):
        (l, r, num) = v
        dist = r - l + 1
        if (num, -dist) > best:
            best = (num, -dist)
            bestv = v

    print(bestv[0] + 1, bestv[1] + 1)


def __starting_point():
    main()


__starting_point()
