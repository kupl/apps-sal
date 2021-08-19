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
import resource

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
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


class DQ():
    def __init__(self):
        self.q = []
        self.d = []

    def add(self, x):
        heapq.heappush(self.q, x)

    def rem(self, x):
        heapq.heappush(self.d, x)

    def top(self):
        while self.d and self.q[0] == self.d[0]:
            heapq.heappop(self.q)
            heapq.heappop(self.d)

        if self.q:
            return self.q[0]

        return None


def main():
    n, q = LI()
    ab = [LI() for _ in range(n)]
    cd = [LI() for _ in range(q)]

    m = 2 * 10**5 + 1
    r = DQ()
    t = [DQ() for _ in range(m)]
    ca = [-1] * (n + 1)
    e = [-1] * (n + 1)

    for c in range(1, n + 1):
        a, b = ab[c - 1]
        ca[c] = a
        e[c] = b
        tp = t[b].top()
        if tp:
            s = -tp
            if s < a:
                r.rem(s)
                r.add(a)
            t[b].add(-a)
        else:
            r.add(a)
            t[b].add(-a)

        # print("ab",a,b,r.q,r.d)

    rr = []
    for c, d in cd:
        a = ca[c]
        b = e[c]
        e[c] = d
        s = -t[b].top()
        t[b].rem(-a)
        if s == a:
            r.rem(a)
            u = t[b].top()
            if not u is None:
                r.add(-u)

        tp = t[d].top()
        if tp:
            s = -tp
            if s < a:
                r.rem(s)
                r.add(a)
            t[d].add(-a)
        else:
            r.add(a)
            t[d].add(-a)

        # print("cd", c,d,r.q,r.d)
        rr.append(r.top())

    return JA(rr, "\n")


print(main())
