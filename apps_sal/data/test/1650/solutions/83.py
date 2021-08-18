L = input()
l = len(L)
dp = [[0] * 2 for _ in range(100005)]
dp[0][0] = 1
mod = 10**9 + 7

for i in range(l):
    n = L[i]
    if n == "0":
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % mod

    if n == "0":
        dp[i + 1][1] += dp[i][1] * 2 % mod
    else:
        dp[i + 1][0] += dp[i][0] * 2 % mod
        dp[i + 1][1] += dp[i][1] * 2 % mod

print((dp[l][0] + dp[l][1]) % mod)
