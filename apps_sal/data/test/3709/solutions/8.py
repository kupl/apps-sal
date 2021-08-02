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
eps = 1.0 / 10**15
mod = 10**9 + 7


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n, k = LI()
    s = set()
    for _ in range(n):
        t = LI()
        c = sum(t)
        if c == 0:
            return 'YES'
        s.add(tuple(t))

    l = list(s)
    ll = len(s)
    for i in range(ll):
        for j in range(i + 1, ll):
            f = True
            for li in range(k):
                if l[i][li] == 1 and l[j][li] == 1:
                    f = False
                    break
            if f:
                return 'YES'

    return 'NO'


print(main())
