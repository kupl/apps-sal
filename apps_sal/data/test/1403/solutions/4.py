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
    n, k = LI()
    a = collections.Counter(LI())
    r = n
    ks = sorted(a.keys())
    for i in range(len(ks) - 1):
        k1 = ks[i]
        k2 = ks[i + 1]
        if k1 < k2 and k1 + k >= k2:
            r -= a[k1]

    return r


print(main())
