(N, K) = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(K)]
dp = [0] * (N + 1)
a = [0] * (N + 1)
dp[1] = 1
a[1] = 1
mod = 998244353
for i in range(1, N + 1):
    for (l, r) in lr:
        if i - l > 0:
            dp[i] += a[i - l]
        if i - r - 1 > 0:
            dp[i] -= a[i - r - 1]
    dp[i] %= mod
    a[i] = a[i - 1] + dp[i]
    a[i] %= mod
print(dp[N])
