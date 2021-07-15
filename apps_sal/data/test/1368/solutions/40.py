import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, A, B = map(int, input().split())
V = list(map(int, input().split()))

dp = [-1] * (N + 1)
dp[0] = 0
cnt = [0] * (N + 1)
cnt[0] = 1

for i in range(N):
    for j in range(N, 0, -1):
        if dp[j - 1] < 0:
            continue
        if dp[j] < dp[j - 1] + V[i]:
            dp[j] = dp[j - 1] + V[i]
            cnt[j] = cnt[j - 1]
        elif dp[j] == dp[j - 1] + V[i]:
            cnt[j] += cnt[j - 1]

up = -1
btm = -1
s = 0

for i in range(A, B + 1):
    if dp[i] < 0:
        continue
    if up < 0:
        up, btm = dp[i], i
        s = cnt[i]
    elif up * i < dp[i] * btm:
        up, btm = dp[i], i
        s = cnt[i]
    elif up * i == dp[i] * btm:
        s += cnt[i]


print(up / btm)
print(s)
