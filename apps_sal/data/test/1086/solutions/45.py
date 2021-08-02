import numpy as np

H, W = map(int, input().split())
A = np.zeros((H, W))
for c in [1, -1]:
    for i in range(H):
        num = list(map(int, input().split()))
        A[i, :] += np.array(num) * c

M = 160 * 80
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1 << M
for i in range(H):
    for j in range(W):
        if i > 0:
            dp[i][j] |= dp[i - 1][j]
        if j > 0:
            dp[i][j] |= dp[i][j - 1]
        a = abs(A[i, j])
        dp[i][j] = (dp[i][j] << int(a)) | (dp[i][j] >> int(a))
i = M
while True:
    if (dp[H - 1][W - 1] >> i) & 1:
        print(i - M)
        break
    i += 1
