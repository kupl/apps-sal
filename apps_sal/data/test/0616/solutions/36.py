import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits


def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, M = MAP()

key_lis = []
key_cost = []

for _ in range(M):
    a, b = MAP()
    c = LIST()
    key = 0
    for x in c:
        key += 2**(x - 1)
    key_lis.append(key)
    key_cost.append(a)


dp = [INF] * (1 << N)
dp[0] = 0

for S in range(1 << N):
    for i, key in enumerate(key_lis):
        dp[S | key] = min(dp[S | key], dp[S] + key_cost[i])

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
