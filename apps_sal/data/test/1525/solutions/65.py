H, W, K = [int(x) for x in input().split()]
p = 10 ** 9 + 7

# H = 1, 縦棒W本のあみだくじの数　→フィボナッチ数列
h1amida = [1, 1, 2] + [None] * 6
for i in range(3, 9):
    h1amida[i] = h1amida[i - 2] + h1amida[i - 1]

# dp[h][k] = 縦棒の長さh+1、縦棒の本数W、ゴールの棒kとなるあみだの数
# dp[0][*]とdp[*][0]はダミー
dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]

for k in range(1, W + 1):
    if k == 1:
        dp[1][k] = h1amida[W - 1]
    elif k == 2:
        dp[1][k] = h1amida[W - 2]
    else:
        dp[1][k] = 0

for h in range(2, H + 1):
    for k in range(1, W + 1):
        if k > 1:
            dp[h][k] += (dp[h - 1][k - 1] * h1amida[k - 2] % p) * h1amida[W - k] % p
        dp[h][k] += (dp[h - 1][k] * h1amida[k - 1] % p) * h1amida[W - k] % p
        if k < W:
            dp[h][k] += (dp[h - 1][k + 1] * h1amida[k - 1] % p) * h1amida[W - k - 1] % p
        dp[h][k] %= p

print((dp[H][K]))

