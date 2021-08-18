H, W, K = list(map(int, input().split()))

WW = [0] * (W + 1)
WW[0] = 1
WW[1] = 1
for i in range(2, W + 1):
    WW[i] = WW[i - 1] + WW[i - 2]
DP = [[0] * W for i in range(H + 1)]
DP[0][0] = 1
mod = 10**9 + 7
for i in range(1, H + 1):
    for j in range(W):
        if j == 0:
            DP[i][j] = DP[i - 1][j] * WW[W - 1]
            if W > 1:
                DP[i][j] += DP[i - 1][j + 1] * WW[W - 2]
        elif j == W - 1:
            DP[i][j] = DP[i - 1][j] * WW[W - 1]
            if W > 1:
                DP[i][j] += DP[i - 1][j - 1] * WW[W - 2]
        else:
            DP[i][j] = DP[i - 1][j] * WW[j] * WW[W - 1 - j] + DP[i - 1][j - 1] * \
                WW[j - 1] * WW[W - 1 - j] + DP[i - 1][j + 1] * WW[j] * WW[W - 2 - j]

        DP[i][j] %= mod
print((DP[-1][K - 1]))
