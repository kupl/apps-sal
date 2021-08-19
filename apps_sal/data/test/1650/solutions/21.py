# coding: utf-8
# Your code here!
L = input()

N = len(L)

dp = [[0 for i in range(2)] for j in range(N)]
dp[0][0] = 1
dp[0][1] = 2
# print(dp)

mod = 10**9 + 7
for i in range(N - 1):
    dp[i + 1][0] = (3 * dp[i][0] + (0 if L[i + 1] == "0" else dp[i][1])) % mod
    dp[i + 1][1] = (dp[i][1] if L[i + 1] == "0" else 2 * dp[i][1]) % mod


# print(dp)
print(((dp[-1][0] + dp[-1][1]) % mod))
