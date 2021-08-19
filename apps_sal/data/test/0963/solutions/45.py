(n, k) = map(int, input().split())
mod = 998244353
lr = [list(map(int, input().split())) for i in range(k)]
dp = [0] * (n + 1)
dp[1] = 1
cum = [0] * (n + 1)
cum[1] = 1
for i in range(2, n + 1):
    for (l, r) in lr:
        li = max(i - r, 1)
        ri = i - l
        if ri < 0:
            continue
        dp[i] += cum[ri] - cum[li - 1]
        dp[i] %= mod
    cum[i] = dp[i] + cum[i - 1]
    cum[i] %= mod
print(dp[n] % mod)
