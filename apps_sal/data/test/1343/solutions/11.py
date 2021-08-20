from itertools import product
from math import ceil, floor, factorial, fsum, isinf, exp, log, log10, log2, isfinite
from collections import Counter
import sys
sys.setrecursionlimit(20000)


def getlist(tcast):
    return [tcast(x) for x in input().strip().split(' ')]


def getval(tcast):
    return tcast(input().strip())


def getmatrix(r, tcast):
    mat = []
    for i in range(r):
        mat.append(getlist(tcast))
    return mat


def isodd(n):
    return n & 1


def numdigits(n):
    return len(str(n)) - (1 if n < 0 else 0)


def primesupto(n):
    isp = [True] * (n + 1)
    (isp[0], isp[1]) = (False, False)
    for (i, x) in enumerate(isp):
        if x:
            mults = i * i
            while mults <= n:
                isp[mults] = False
                mults += i
    return isp


def maxarrays(a, b):
    return [max(x, y) for (x, y) in zip(a, b)]


(nv, ne, ns) = getlist(int)
if ns == 0 or ne == 0:
    print(-1)
else:
    edges = []
    for i in range(ne):
        (start, end, weight) = getlist(int)
        edges.append((start, end, weight))
    starts = getlist(int)
    checkstart = set(starts)
    best = 100000000000000000
    cur = 0
    for edge in edges:
        (a, b) = (edge[0], edge[1])
        if a in checkstart and b not in checkstart or (b in checkstart and a not in checkstart):
            best = min(best, edge[2])
    print(-1 if best == 100000000000000000 else best)
