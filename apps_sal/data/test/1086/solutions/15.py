import numpy as np

H, W = list(map(int, input().split()))
As = [list(map(int, input().split())) for _ in range(H)]
Bs = [list(map(int, input().split())) for _ in range(H)]

ds = [[abs(A - B) for A, B in zip(row_A, row_B)] for row_A, row_B in zip(As, Bs)]

size = 10005

dp = np.full((H, W, size), False)
dp[0][0][ds[0][0]] = True
for i in range(H):
    for j in range(W):
        if i + 1 < H:
            d = ds[i + 1][j]
            dp[i + 1][j][d:] = np.logical_or(dp[i][j][:size - d], dp[i + 1][j][d:])
            dp[i + 1][j][:size - d] = np.logical_or(dp[i][j][d:], dp[i + 1][j][:size - d])
            dp[i + 1][j][:d + 1] = np.logical_or(dp[i][j][d::-1], dp[i + 1][j][:d + 1])
        if j + 1 < W:
            d = ds[i][j + 1]
            dp[i][j + 1][d:] = np.logical_or(dp[i][j][:size - d], dp[i][j + 1][d:])
            dp[i][j + 1][:size - d] = np.logical_or(dp[i][j][d:], dp[i][j + 1][:size - d])
            dp[i][j + 1][:d + 1] = np.logical_or(dp[i][j][d::-1], dp[i][j + 1][:d + 1])

print((np.min(np.where(dp[-1][-1]))))
