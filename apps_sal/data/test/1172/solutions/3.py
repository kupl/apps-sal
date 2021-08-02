#!/usr/bin/env python3

s = str(input())

mod = 10**9 + 7
dp = [[0] * 4 for i in range(len(s) + 1)]
dp[0][0] = 1
for i in range(1, len(s) + 1):
    for j in range(4):
        if s[i - 1] == "?":
            dp[i][j] = (dp[i - 1][j] * 3) % mod
        else:
            dp[i][j] = (dp[i - 1][j]) % mod

    if s[i - 1] == "A":
        dp[i][1] += (dp[i - 1][0]) % mod
    elif s[i - 1] == "B":
        dp[i][2] += (dp[i - 1][1]) % mod
    elif s[i - 1] == "C":
        dp[i][3] += (dp[i - 1][2]) % mod
    else:
        dp[i][1] += (dp[i - 1][0]) % mod
        dp[i][2] += (dp[i - 1][1]) % mod
        dp[i][3] += (dp[i - 1][2]) % mod

# print(dp)
print((dp[-1][-1] % mod))
