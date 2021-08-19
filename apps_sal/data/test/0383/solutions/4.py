import random
import sys
Q = 10 ** 9 + 7
(n, k, d) = map(int, input().split())
dp = [0] * 105
dp1 = [0] * 105
dp[0] = 1
dp1[0] = 1
for i in range(1, n + 1):
    for j in range(max(0, i - k), i):
        dp[i] = dp[i] + dp[j]
    for j in range(max(0, i - d + 1), i):
        dp1[i] = dp1[i] + dp1[j]
print((dp[n] - dp1[n]) % Q)
