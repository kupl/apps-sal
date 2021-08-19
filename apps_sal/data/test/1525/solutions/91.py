(H, W, K) = list(map(int, input().split()))
mod = 10 ** 9 + 7
dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        for bit in range(1 << W - 1):
            ok = True
            for k in range(W - 2):
                if bit & 1 << k and bit & 1 << k + 1:
                    ok = False
            if not ok:
                continue
            jj = j
            if j > 0 and bit & 1 << j - 1:
                jj -= 1
            elif j < W - 1 and bit & 1 << j:
                jj += 1
            dp[i + 1][jj] += dp[i][j]
            dp[i + 1][jj] %= mod
print(dp[H][K - 1])
