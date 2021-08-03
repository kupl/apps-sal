MOD = 10 ** 9 + 7
h, w, k = [int(x) for x in input().split()]
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for b in range(1 << (w - 1)):
        ok = True
        for s in range(w - 2):
            if b >> s & 1 and b >> (s + 1) & 1:
                ok = False
        if ok:
            for j in range(w):
                if j > 0 and b >> (j - 1) & 1:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
                elif j + 1 < w and b >> j & 1:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
                else:
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD

print(dp[h][k - 1])
