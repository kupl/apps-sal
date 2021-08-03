import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    a = [S() for _ in range(n)]
    d = collections.defaultdict(int)
    for c in a:
        k = 0
        lk = 0
        for t in c:
            if t == ')':
                k += 1
                if lk < k:
                    lk = k
            else:
                k -= 1
        k = 0
        rk = 0
        for t in c[::-1]:
            if t == '(':
                k += 1
                if rk < k:
                    rk = k
            else:
                k -= 1
        if lk > 0 and rk > 0:
            continue
        if lk == 0 and rk == 0:
            d[0] += 1
        if lk > 0:
            d[-lk] += 1
        if rk > 0:
            d[rk] += 1

    r = d[0] ** 2
    for k in list(d.keys()):
        if k <= 0:
            continue
        r += d[k] * d[-k]

    return r


print(main())
