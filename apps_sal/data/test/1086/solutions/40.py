H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]

dp = [[0] * W for i in range(H)]
dp[0][0] = 1 << (abs(A[0][0] - B[0][0]) + 6400)
for i in range(H):
    for j in range(W):
        d = abs(A[i][j] - B[i][j])
        if i > 0:
            dp[i][j] |= dp[i - 1][j] << d | dp[i - 1][j] >> d
        if j > 0:
            dp[i][j] |= dp[i][j - 1] << d | dp[i][j - 1] >> d
ans = 0
res = dp[H - 1][W - 1] >> 6400
while res & 1 == 0:
    res >>= 1
    ans += 1
print(ans)

