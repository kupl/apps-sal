MOD = 10 ** 9 + 7
l = input()
p = len(l)
dp = [[0, 0] for _ in range(p)]
dp[0] = [1, 2]
for (i, s) in enumerate(l[1:], start=1):
    if s == '1':
        dp[i][0] = dp[i - 1][0] * 3 + dp[i - 1][1]
        dp[i][1] = dp[i - 1][1] * 2
    else:
        dp[i][0] = dp[i - 1][0] * 3
        dp[i][1] = dp[i - 1][1]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
ans = sum(dp[-1])
print(ans % MOD)
