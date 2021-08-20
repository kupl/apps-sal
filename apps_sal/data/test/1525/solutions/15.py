(h, w, k) = list(map(int, input().split()))
k -= 1
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
mod = 10 ** 9 + 7


def cnt(n):
    if n < 0:
        return 1
    if 0 <= n < 3:
        return n + 1
    return n + (n - 1) * (n - 2) // 2 + (n - 2) * (n - 3) * (n - 4) // 6 + 1


for i in range(h):
    for j in range(w):
        if j > 0:
            dp[i + 1][j - 1] += dp[i][j] * cnt(j - 2) * cnt(w - 2 - j)
            dp[i + 1][j - 1] %= mod
        if j < w - 1:
            dp[i + 1][j + 1] += dp[i][j] * cnt(j - 1) * cnt(w - 3 - j)
            dp[i + 1][j + 1] %= mod
        dp[i + 1][j] += dp[i][j] * cnt(j - 1) * cnt(w - 2 - j)
        dp[i + 1][j] %= mod
print(dp[h][k])
