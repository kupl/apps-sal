import numpy as np
(H, W) = list(map(int, input().split()))
A = [[0] * W for i in range(H)]
B = [[0] * W for i in range(H)]
for i in range(H):
    inf = [int(c) for c in input().split()]
    for j in range(W):
        A[i][j] = inf[j]
for i in range(H):
    inf = [int(c) for c in input().split()]
    for j in range(W):
        B[i][j] = inf[j]
X = (H + W) * 80
L = X + X + 1
dp = [[0] * W for _ in range(H)]
d = abs(A[0][0] - B[0][0])
dp[0][0] = np.zeros(L, np.bool)
dp[0][0][X + d] = 1
for h in range(H):
    for (w, (a, b)) in enumerate(zip(A[h], B[h])):
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
dp2 = dp[-1][-1]
can_make = np.where(dp2)[0] - X
answer = np.abs(can_make).min()
print(answer)
