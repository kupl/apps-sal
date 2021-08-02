#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def solve():
    n = I()
    v = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    d = [0] * n
    d[0] = 1
    q = deque([0])
    p = [None] * n
    while q:
        x = q.popleft()
        nd = d[x] + 1
        for y in v[x]:
            if not d[y]:
                d[y] = nd
                p[y] = x
                q.append(y)
    V = list(range(n))
    V.sort(key=lambda x: -d[x])
    t = [1] * n
    for x in V[:-1]:
        t[p[x]] += t[x]
    ans = 0
    p = pow(2, n - 1, mod)
    for x in range(n):
        tx = t[x]
        if len(v[x]) < 2:
            continue
        s = p - 1
        for y in v[x]:
            ty = t[y]
            if tx < ty:
                s -= pow(2, t[0] - tx, mod) - 1
            else:
                s -= pow(2, ty, mod) - 1
            s %= mod
        ans += s
        ans %= mod
    print((ans * pow(2, (mod - 2) * n % (mod - 1), mod) % mod))
    return

# Solve


def __starting_point():
    solve()


__starting_point()
