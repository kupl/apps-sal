H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]
B = [tuple(map(int, input().split())) for _ in range(H)]

C = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]

D = 80 * (H + W) + 1
D2 = D * 2

dp = [[0] * W for _ in range(H)]

dp[0][0] |= 1 << (D + C[0][0])
dp[0][0] |= 1 << (D - C[0][0])

for h in range(H):
    for w in range(W):
        c = C[h][w]
        if h >= 1:
            dp[h][w] |= dp[h - 1][w] << c
            dp[h][w] |= dp[h - 1][w] >> c
        if w >= 1:
            dp[h][w] |= dp[h][w - 1] << c
            dp[h][w] |= dp[h][w - 1] >> c

ans = D2
tmp = dp[H - 1][W - 1]

for i in range(D2):
    if (tmp >> i) & 1:
        ans = min(ans, abs(i - D))

print (ans)
