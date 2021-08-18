

import sys
readline = sys.stdin.readline

L = readline().rstrip()
keta = len(L)
DIV = 10 ** 9 + 7

dp = [[0] * 2 for i in range(keta)]
dp[0][0] = 2
dp[0][1] = 1

for i in range(1, keta):
    x = L[i]
    if x == "1":
        dp[i][0] += dp[i - 1][0] * 2
        dp[i][1] += dp[i - 1][0] * 1
        dp[i][0] %= DIV
        dp[i][1] %= DIV
    else:
        dp[i][0] += dp[i - 1][0] * 1
        dp[i][0] %= DIV
    dp[i][1] += dp[i - 1][1] * 3
    dp[i][1] %= DIV

print((dp[keta - 1][0] + dp[keta - 1][1]) % DIV)
