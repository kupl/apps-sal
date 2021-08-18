
import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/28 22:46

"""

MOD = 998244353
N = int(input())
S = input()
rem = {S[0], S[-1]}

ans = 0
for v in rem:
    l, r = 0, N - 1
    while l < N and S[l] == v:
        l += 1

    while r >= 0 and S[r] == v:
        r -= 1

    if l > r:
        ans += N * (N - 1) // 2
        ans %= MOD
    else:
        ans += (l + 1) * (N - r)
        ans %= MOD
ans = (ans + MOD - len(rem) + 1) % MOD
print(ans)
