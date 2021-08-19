w = [1, 2]
for i in range(6):
    w.append(w[-2] + w[-1])
(H, W, K) = map(int, input().split())
mod = 10 ** 9 + 7
dp = [[0 for i in range(W)] for j in range(H + 1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if j >= 1:
            k = 1
            if j - 2 >= 0:
                k *= w[j - 2]
            if W - j - 2 >= 0:
                k *= w[W - j - 2]
            dp[i + 1][j - 1] += k * dp[i][j]
            dp[i + 1][j - 1] %= mod
        k = 1
        if j - 1 >= 0:
            k *= w[j - 1]
        if W - j - 2 >= 0:
            k *= w[W - j - 2]
        dp[i + 1][j] += k * dp[i][j]
        dp[i + 1][j] %= mod
        if j <= W - 2:
            k = 1
            if j - 1 >= 0:
                k *= w[j - 1]
            if W - j - 3 >= 0:
                k *= w[W - j - 3]
            dp[i + 1][j + 1] += k * dp[i][j]
            dp[i + 1][j + 1] %= mod
print(dp[H][K - 1] % mod)
