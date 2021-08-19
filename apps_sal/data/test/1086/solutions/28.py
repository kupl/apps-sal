import numpy as np
(H, W, *L) = map(int, open(0).read().split())
A = L[:H * W]
B = L[H * W:]
C = [abs(b - a) for (a, b) in zip(A, B)]
U = max(C) * (H + W)
N = 2 * U + 1
INF = 10 ** 10
dp = np.zeros((H, W, N), dtype=bool)
dp[0, 0, C[0] + U] = True
for i in range(1, W):
    c = C[i]
    dp[0, i, c:] |= dp[0, i - 1, :N - c]
    dp[0, i, :N - c] |= dp[0, i - 1, c:]
for i in range(1, H):
    c = C[i * W]
    dp[i, 0, c:] |= dp[i - 1, 0, :N - c]
    dp[i, 0, :N - c] |= dp[i - 1, 0, c:]
for i in range(1, H):
    for j in range(1, W):
        c = C[i * W + j]
        dp[i, j, c:] |= dp[i, j - 1, :N - c]
        dp[i, j, :N - c] |= dp[i, j - 1, c:]
        dp[i, j, c:] |= dp[i - 1, j, :N - c]
        dp[i, j, :N - c] |= dp[i - 1, j, c:]
ans = np.min(np.abs(np.where(dp[H - 1][W - 1])[0] - U))
print(ans)
