(h, w, k) = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
dp = [[0 for _ in range(w)] for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for bit in range(1 << w - 1):
        if '11' in bin(bit):
            continue
        for j in range(w):
            if j > 0 and bit & 1 << j - 1:
                dp[i + 1][j - 1] += dp[i][j] % mod
            elif bit & 1 << j:
                dp[i + 1][j + 1] += dp[i][j] % mod
            else:
                dp[i + 1][j] += dp[i][j] % mod
print(dp[h][k - 1] % mod)
