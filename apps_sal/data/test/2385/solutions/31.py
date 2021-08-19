# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:56:10 2020
"""

import sys
#import numpy as np

sys.setrecursionlimit(10 ** 9)
# def input():
#    return sys.stdin.readline()[:-1]
mod = 10**9 + 7

N = int(input())
#X, Y = map(int,input().split())
ab = [list(map(int, input().split())) for i in range(N - 1)]

fact = [1, 1]  # 元テーブル
fact_inv = [1, 1]  # 逆元テーブル
tmp_inv = [0, 1]  # 逆元テーブル計算用テーブル
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    tmp_inv.append((-tmp_inv[mod % i] * (mod // i)) % mod)
    fact_inv.append((fact_inv[-1] * tmp_inv[-1]) % mod)


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % mod
# 逆元作成


def inv(a, mod):
    return pow(a, mod - 2, mod)


graph = [[] for _ in range(N + 1)]
for a, b in ab:
    graph[a].append(b)
    graph[b].append(a)

root = 1
parent = [0] * (N + 1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if parent[x] == y:
            continue
        parent[y] = x
        stack.append(y)

size_d = [0] * (N + 1)
dp_d = [1] * (N + 1)
for v in order[::-1]:
    dp_d[v] *= fact[size_d[v]]
    dp_d[v] %= mod
    p = parent[v]
    s = size_d[v] + 1
    size_d[p] += s
    dp_d[p] *= fact_inv[s] * dp_d[v]
    dp_d[p] %= mod

size_u = [N - x - 1 for x in size_d]
dp_u = [1] * (N + 1)
for v in order[1:]:
    p = parent[v]
    x = dp_d[p] * inv(dp_d[v], mod)
    x *= fact_inv[size_d[p]] * fact[size_d[v] + 1]
    x *= fact[size_u[v] - 1] * fact_inv[size_u[p]]
    x *= dp_u[p]
    dp_u[v] = x % mod

for xd, xu, sd, su in zip(dp_d[1:], dp_u[1:], size_d[1:], size_u[1:]):
    x = xd * xu * fact[sd + su] * fact_inv[sd] * fact_inv[su] % mod
    print(x)
