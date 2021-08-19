from decimal import ROUND_HALF_UP, Decimal
from collections import deque, Counter, defaultdict
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10 ** 9 + 7
inf = float('inf')


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)
n = int(input())
ans = -inf
F = []
P = []
for i in range(n):
    F.append(list(map(int, input().split())))
for i in range(n):
    P.append(list(map(int, input().split())))
for bit in range(1, 1 << 10):
    L = [bit >> i & 1 for i in range(10)]
    now = 0
    for i in range(n):
        cnt = 0
        for cc in range(10):
            if F[i][cc] == 1 and L[cc] == 1:
                cnt += 1
        now += P[i][cnt]
    ans = max(ans, now)
print(ans)
