H, W, K = list(map(int, input().split()))
mod = 1000000007

f = [0] * (W + 1)
f[0] = 1
f[1] = 2
for i in range(2, W + 1):
    f[i] = f[i - 1] + f[i - 2]

dp = [[0] * (W + 2) for _ in range(H + 1)]
dp[0][K] = 1
for i in range(1, H + 1):
    for j in range(1, W + 1):
        dp[i][j] += (dp[i - 1][j] * f[max(0, j - 2)] * f[max(0, W - j - 1)]
                     + dp[i - 1][j - 1] * f[max(0, j - 3)] * f[max(0, W - j - 1)]
                     + dp[i - 1][j + 1] * f[max(0, j - 2)] * f[max(0, W - j - 2)])
        dp[i][j] %= mod
print(dp[-1][1])
