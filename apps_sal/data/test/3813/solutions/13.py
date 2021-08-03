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
mod = 10**9 + 7


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    p = LI_()
    x = LI()
    e = collections.defaultdict(list)
    for i in range(n - 1):
        e[p[i]].append(i + 1)

    def f(i):
        if not e[i]:
            return [0, x[i]]
        a = 0
        xi = x[i]
        xi1 = xi + 1
        tx = [0] * xi1
        tx[0] = 1
        for c in e[i]:
            rc = f(c)
            if not rc:
                return
            a += sum(rc)
            tt = [0] * xi1
            for i in range(xi1):
                if tx[i] == 0:
                    continue
                for c in rc:
                    if i + c < xi1:
                        tt[i + c] = 1
            tx = tt
        for i in range(xi, -1, -1):
            if tx[i] == 1:
                return [xi, a - i]
        return

    if f(0):
        return 'POSSIBLE'

    return 'IMPOSSIBLE'


print((main()))
