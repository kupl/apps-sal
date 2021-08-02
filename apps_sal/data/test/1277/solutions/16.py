#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10 ** 5 + 1)


def dfsu(s, p):
    for t in g[s]:
        if t == p:
            continue
        du[t] = du[s] + 1
        dfsu(t, s)


def dfsv(s, p):
    for t in g[s]:
        if t == p:
            continue
        dv[t] = dv[s] + 1
        dfsv(t, s)


n, u, v = list(map(int, input().split()))
u -= 1
v -= 1
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    g[a].append(b)
    g[b].append(a)

du = [0] * n
dv = [0] * n
dfsu(u, -1)
dfsv(v, -1)

mx = 0
for i in range(n):
    if du[i] < dv[i]:
        mx = max(mx, dv[i])
print((mx - 1))
