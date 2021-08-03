L = str(input())
ls = len(L)
cnt = 0
ans = 0
MOD = 10**9 + 7
dp = [[0, 0] for i in range(ls + 1)]
dp[0][0] = 1
for i in range(ls):
    dp[i + 1][1] += 3 * dp[i][1]
    if L[i] == "1":
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][0] += 2 * dp[i][0]
    else:
        dp[i + 1][0] += dp[i][0]
    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD

ans = sum(dp[-1]) % MOD
print(ans)
