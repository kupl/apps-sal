# 実はDPと割り切るとわかりやすい
mod = 10**9 + 7
h, w, K = map(int, input().split())
dp = [[0] * w for j in range(h + 1)]
dp[0][0] = 1
for i in range(1, h + 1):
    for k in range(2**(w - 1)):
        for l in range(w - 2):
            if ((k >> l) & 1) and ((k >> (l + 1)) & 1):
                break
        else:
            for l in range(w):
                if l == 0:
                    if ((k >> l) & 1):
                        dp[i][l + 1] += dp[i - 1][l]
                    else:
                        dp[i][l] += dp[i - 1][l]
                elif l == w - 1:
                    if ((k >> (l - 1)) & 1):
                        dp[i][l - 1] += dp[i - 1][l]
                    else:
                        dp[i][l] += dp[i - 1][l]
                else:
                    if ((k >> l) & 1) or ((k >> (l - 1)) & 1):
                        if ((k >> l) & 1):
                            dp[i][l + 1] += dp[i - 1][l]
                        else:
                            dp[i][l - 1] += dp[i - 1][l]
                    else:
                        dp[i][l] += dp[i - 1][l]
            dp[i][l] %= mod
print(dp[h][K - 1] % mod)
