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
import copy
import functools
import time
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    h, w, k = LI()
    aa = [[int(c) for c in S()] for _ in range(h)]

    def f(hs):
        l = len(hs)
        c = [0] * l
        r = l - 1
        for i in range(w):
            nc = [0] * l
            bf = False
            for j in range(l):
                for h in hs[j]:
                    nc[j] += aa[h][i]
                if nc[j] > k:
                    return -1
                if nc[j] + c[j] > k:
                    bf = True
            if bf:
                r += 1
                c = nc
            else:
                for j in range(l):
                    c[j] += nc[j]
        return r

    r = inf
    for bi in range(2**(h - 1)):
        hs = [[0]]
        for i in range(h - 1):
            if 2**i & bi > 0:
                hs.append([])
            hs[-1].append(i + 1)
        t = f(hs)
        if t >= 0 and r > t:
            r = t

    return r


print(main())
