import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int, input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int, input().split()))
def lcm(a, b): return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 6)
mod = 10**9 + 7
cnt = 0
ans = 0
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

N = k()
edge = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = I()
    edge[a].append((b, c))
    edge[b].append((a, c))

Q, K = I()

dist = [None] * (N + 1)


def dfs(x, d):
    dist[x] = d
    for y, dd in edge[x]:
        if dist[y] is not None:
            continue
        dfs(y, d + dd)


dfs(K, 0)
for _ in range(Q):
    x, y = I()
    print(dist[x] + dist[y])
