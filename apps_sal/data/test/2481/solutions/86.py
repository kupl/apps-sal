import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int, input().split())
def L(): return list(input().split())
def l(): return list(map(int, input().split()))
def lcm(a, b): return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9 + 7

H, W = I()
cost = [l() for _ in range(10)]
A = [l() for _ in range(H)]
ans = 0
for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for i in range(H):
    for j in range(W):
        if A[i][j] > -1:
            ans += cost[A[i][j]][1]
print(ans)
