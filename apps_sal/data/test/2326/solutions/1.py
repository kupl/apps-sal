from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


MAX = 10000
MOD = 998244353
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX


def COMinit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1;
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    return None


def COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


N = read()
A = readlist()

for i in range(N):
    A[i] = max(0, A[i])
    if A[i] > N - i - 1:
        A[i] = 0

COMinit()

dp = [0] * N

for n in range(1, N):
    dp[n] = dp[n - 1]
    for i in range(n):
        if i == 0:
            dp[n] = (dp[n] + COM(n - i - 1, A[i] - 1)) % MOD
        else:
            dp[n] = (dp[n] + COM(n - i - 1, A[i] - 1) * (dp[i - 1] + 1)) % MOD

print(dp[N - 1])
