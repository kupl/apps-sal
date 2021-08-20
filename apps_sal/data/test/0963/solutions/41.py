mod = 998244353
(n, k) = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(k)]
dp = [0] * n
cum = [0] * n
dp[0] = 1
cum[0] = 1
for i in range(n):
    for (l, r) in lr:
        if i - l >= 0:
            dp[i] += cum[i - l]
        if i - r - 1 >= 0:
            dp[i] -= cum[i - r - 1]
        dp[i] %= mod
        cum[i] = cum[i - 1] + dp[i]
        cum[i] %= mod
print(dp[-1] % mod)
