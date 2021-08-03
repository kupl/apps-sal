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

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return tuple(map(int, sys.stdin.readline().split()))
def LLI(): return [tuple(map(int, l.split())) for l in sys.stdin]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n, m = LI()
    a = [LI() for _ in range(n)]
    b = [LI() for _ in range(n)]
    for i in range(n):
        t = 0
        for j in range(m):
            if a[i][j] != b[i][j]:
                t += 1
        if t % 2 == 1:
            return 'No'

    for j in range(m):
        t = 0
        for i in range(n):
            if a[i][j] != b[i][j]:
                t += 1
        if t % 2 == 1:
            return 'No'

    return 'Yes'


print(main())
