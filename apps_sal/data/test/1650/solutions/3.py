L = input()
n = len(L)
mod = 1000000007
dp = [[0, 0] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    dp[i + 1][1] += 3 * dp[i][1] % mod
    dp[i + 1][1] %= mod
    if L[i] == "1":
        dp[i + 1][0] += 2 * dp[i][0]
        dp[i + 1][0] %= mod
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][1] %= mod
    else:
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][0] %= mod
ans = (dp[n][0] + dp[n][1]) % mod
print(ans)
