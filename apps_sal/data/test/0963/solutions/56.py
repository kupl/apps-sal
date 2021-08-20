mod = 998244353
(n, k, *LR) = map(int, open(0).read().split())
dp = [0] * (3 * n)
dp[1] = 1
dp[2] = -1
for i in range(1, n + 1):
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
    for (l, r) in zip(LR[::2], LR[1::2]):
        dp[i + l] += dp[i]
        dp[i + l] %= mod
        dp[i + r + 1] -= dp[i]
        dp[i + r + 1] %= mod
print(dp[n])
