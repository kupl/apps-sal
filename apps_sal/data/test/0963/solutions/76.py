(n, k) = map(int, input().split())
mod = 998244353
dp = [0] * (n * 3)
lr = []
for _ in range(k):
    (l, r) = map(int, input().split())
    lr.append((l, r))
lr.sort()
imos = [0] * (n * 3)
imos[1] = 1
dp[1] = 1
for i in range(1, n):
    if i >= 2:
        dp[i + 1] += dp[i]
    for (l, r) in lr:
        dp[i + l] += dp[i]
        dp[i + l] %= mod
        dp[i + r + 1] -= dp[i]
        dp[i + r + 1] %= mod
print(dp[n] % mod)
