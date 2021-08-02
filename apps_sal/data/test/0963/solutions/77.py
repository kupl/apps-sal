N, K = map(int, input().split())
mod = 998244353
M = []
for i in range(K):
    l, r = map(int, input().split())
    M.append([l, r])

dp = [0] * (3 * N)
dp[0] = 1
dp[1] = -1
# imos
for i in range(N):
    for l, r in M:
        dp[l + i] += dp[i]
        dp[i + r + 1] -= dp[i]
    dp[i + 1] = (dp[i] + dp[i + 1]) % mod
print(dp[N - 1])
