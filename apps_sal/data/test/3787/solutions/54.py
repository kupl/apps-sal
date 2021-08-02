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
def pf(s): return print(s, flush=True)


def main():
    n, a, b = LI()
    if a + b > n + 1:
        return -1
    t = n // b
    if n % b > 0:
        t += 1
    if a < t:
        return -1
    rr = []
    while n > 0:
        if n == a:
            rr.append(list(range(1, n + 1)))
            break
        if n - b >= a - 1:
            rr.append(list(range(n, n - b, -1)))
            n -= b
            a -= 1
            continue
        rr.append(list(range(n, a - 1, -1)))
        rr.append(list(range(1, a)))
        break
    r = []
    rr.reverse()
    for c in rr:
        r.append(' '.join(map(str, c)))

    return ' '.join(r)


print(main())
