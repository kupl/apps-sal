H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
center = 80 * (H+W)
C = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]

dp = [[0] * W for i in range(H)]
dp[0][0] = (1 << (center + C[0][0])) | (1 >> (center - C[0][0]))

for i in range(H):
    for j in range(W):
        if i:
            dp[i][j] |= dp[i-1][j] << C[i][j]
            dp[i][j] |= dp[i-1][j] >> C[i][j]
        if j:
            dp[i][j] |= dp[i][j-1] << C[i][j]
            dp[i][j] |= dp[i][j-1] >> C[i][j]

ans = center * 2
for i in range(center*2):
    if (dp[H-1][W-1] >> i) & 1:
        ans = min(ans, abs(i-center))

print(ans)

