H, W, K = list(map(int, input().split()))
h_lines = (1, 1, 2, 3, 5, 8, 13, 21, 34)
MOD = 10 ** 9 + 7

dp = [[0] * 8 for _ in range(H + 1)]
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        dp[h + 1][w] = dp[h][w] * h_lines[w] * h_lines[W - w - 1]
        if w > 0:
            dp[h + 1][w] += dp[h][w - 1] * h_lines[w - 1] * h_lines[W - w - 1]
        if w < W - 1:
            dp[h + 1][w] += dp[h][w + 1] * h_lines[w] * h_lines[W - w - 2]
        dp[h + 1][w] %= MOD
print((dp[H][K - 1]))
