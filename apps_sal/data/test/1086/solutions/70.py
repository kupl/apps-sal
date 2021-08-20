import numpy as np
(H, W) = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
X = (H + W) * 80
L = X + X + 1
dp = [[0] * W for _ in range(H)]
d = abs(A[0][0] - B[0][0])
dp[0][0] = np.zeros(L, np.bool)
dp[0][0][X + d] = 1
for h in range(H):
    for w in range(W):
        a = A[h][w]
        b = B[h][w]
        if h == w == 0:
            continue
        d = abs(a - b)
        x = np.zeros(L, np.bool)
        if h != 0:
            x[d:] |= dp[h - 1][w][:L - d]
            x[:L - d] |= dp[h - 1][w][d:]
        if w != 0:
            x[d:] |= dp[h][w - 1][:L - d]
            x[:L - d] |= dp[h][w - 1][d:]
        dp[h][w] = x
dp = dp[-1][-1]
can_make = np.where(dp)[0] - X
answer = np.abs(can_make).min()
print(answer)
