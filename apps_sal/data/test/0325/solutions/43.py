#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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

# A


def A():
    a, b = LI()
    print((max(a + b, a - b, a * b)))
    return

# B


def B():
    k, x = LI()
    ans = []
    for i in range(x - k + 1, x + k):
        ans.append(i)
    print((*ans))
    return

# C


def C():
    def f(s):
        res = [0] * m
        for i in s:
            res[alp.index(i)] += 1
        return res
    alp = list("abcdefghijklmnopqrstuvwxyz")
    m = len(alp)
    n = I()
    s = [input() for i in range(n)]
    d = defaultdict(lambda: 0)
    for i in s:
        d[tuple(f(i))] += 1
    ans = 0
    for i in list(d.values()):
        ans += (i * (i - 1)) // 2
    print(ans)
    return

# D


def D():
    n, m = LI()
    g = LIR(n)
    g.sort(key=lambda x: x[0])
    ans = 0
    f = [1] * n
    j = 0
    q = []
    for i in range(m)[::-1]:
        while j < n and m - g[j][0] >= i:
            a, b = g[j]
            heappush(q, (-b, a))
            j += 1
        if q:
            x, a = heappop(q)
            if i + a <= m:
                ans -= x
    print(ans)
    return

# E


def E():
    def dfs(x, f):
        for y, w in v[x]:
            if f[y]:
                if dp[y] < dp[x] + w:
                    f[y] = 0
                    dp[y] = dp[x] + w
                    dfs(y, f)
                    f[y] = 1
            else:
                if dp[y] < dp[x] + w:
                    dp[y] = float("inf")
                    dfs(y, f)
    n, m, p = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a, b, c = LI()
        a -= 1
        b -= 1
        v[a].append((b, c - p))
    f = [1] * n
    dp = [-float("inf")] * n
    dp[0] = 0
    f[0] = 0
    dfs(0, f)
    ans = dp[n - 1]
    if ans == float("inf") or ans == -float("inf"):
        print((-1))
    elif ans < 0:
        print((0))
    else:
        print(ans)
    return

# F


def F():

    return

# Solve


def __starting_point():
    E()


__starting_point()
