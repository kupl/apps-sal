import sys
from array import array

n, m = list(map(int, input().split()))
dp = [array('i', [0]) * (n + 1) for _ in range(2)]
dp[0][0] = dp[1][0] = 1
mod = 10**9 + 7

for i in range(1, n + 1):
    dp[0][i] = (dp[0][i - 1] * m + dp[0][i - 1] * (m - 1)) % mod
    dp[1][i] = (dp[0][i - 1] * m + dp[1][i - 1] * m) % mod

print(dp[1][-1])
