import sys
input = sys.stdin.readline
(H, W, K) = map(int, input().split())
mod = 10 ** 9 + 7
j = [0, 1, 1, 2, 3, 5, 8, 13]
m = [1, 1, 2, 3, 5, 8, 13, 21]
dp = [[0 for _ in range(W)] for _ in range(H + 1)]
dp[0][0] = 1
for h in range(H + 1):
    for w in range(W):
        if w != 0:
            dp[h][w] += dp[h - 1][w - 1] * j[w] * m[W - 1 - w]
        if w != W - 1:
            dp[h][w] += dp[h - 1][w + 1] * m[w] * j[W - 1 - w]
        dp[h][w] += dp[h - 1][w] * m[w] * m[W - 1 - w]
        dp[h][w] %= mod
print(dp[H][K - 1])
