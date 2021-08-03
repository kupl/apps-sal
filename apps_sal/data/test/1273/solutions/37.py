#!/usr/bin/env python3
from operator import add, itemgetter, mul, xor
from math import gcd
from decimal import Decimal
from copy import deepcopy
from collections import Counter, defaultdict, deque
import numpy as np
import math
import itertools
import heapq
import bisect
import sys
sys.setrecursionlimit(10**7)


def cmb(n, r, mod):
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
        bunshi = bunshi * (n - i) % mod
    return (bunshi * pow(bunbo, mod - 2, mod)) % mod


mod = 10**9 + 7
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return list(map(int, input().split()))
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


n = I()

# graph[i]には頂点iと繋がっている頂点を格納する
graph = [[] for _ in range(n + 1)]
prev_col = [0] * (n + 1)
a_b = []
k = 0
for i in range(n - 1):
    a, b = MI()
    a_b.append(str(a) + " " + str(b))
    graph[a].append(b)
    graph[b].append(a)
# check[i] == -1ならば未探索
check = [-1] * (n + 1)
check[0] = 0
check[1] = 0
for i in range(n + 1):
    k = max(len(graph[i]), k)
d = deque()
d.append(1)
ans = dict()
while d:
    v = d.popleft()
    check[v] = 1
    cnt = 0
    for i in graph[v]:
        if check[i] != -1:
            continue
        cnt = cnt + 1
        if prev_col[v] == cnt:
            cnt = cnt + 1
        prev_col[i] = cnt
        ans[str(min(i, v)) + " " + str(max(i, v))] = cnt
        d.append(i)
print(k)
for key in a_b:
    print((ans[key]))
