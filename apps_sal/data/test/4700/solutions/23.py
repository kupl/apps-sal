import sys
from collections import deque, Counter, defaultdict
import bisect
import heapq
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
inf = 10 ** 18
MOD = 1000000007


def ri():
    return int(input())


def rs():
    return input().strip()


def rl():
    return list(map(int, input().split()))


mod = 998244353
(n, m) = rl()
h = rl()
ans = [1] * n
for i in range(m):
    (a, b) = rl()
    a -= 1
    b -= 1
    if h[a] > h[b]:
        ans[b] = 0
    elif h[a] < h[b]:
        ans[a] = 0
    else:
        (ans[a], ans[b]) = (0, 0)
print(sum(ans))
