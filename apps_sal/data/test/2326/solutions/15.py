# Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open('input.txt', 'r')
MOD = 998244353
sys.setrecursionlimit(1000000)


def ncr(n, r):
    nonlocal f
    return f[n] * pow(f[r], MOD - 2, MOD) * pow(f[n - r], MOD - 2, MOD) % MOD


n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
f = [1]
for i in range(1, n + 1):
    f.append((f[-1] * i) % MOD)
for i in range(n):
    if i + a[i] < n and a[i] > 0: dp[i] = ncr(n - 1 - i, a[i])
for i in reversed(range(n)):
    if a[i] <= 0: continue
    for j in range(i + a[i] + 1, n):
        dp[i] = (dp[i] + ncr(j - 1 - i, a[i]) * dp[j]) % MOD
print(sum(dp) % MOD)
