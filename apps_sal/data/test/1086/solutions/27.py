import numpy as np
(h, w) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]
C = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        C[i][j] = abs(A[i][j] - B[i][j])
d = 80 * (h + w - 1)
D = 2 * d + 1
dp = [[0] * w for j in range(h)]
dp[0][0] = np.zeros(D, np.bool)
dp[0][0][d + C[0][0]] = 1
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        x = np.zeros(D, np.bool)
        if i != 0:
            x[C[i][j]:] |= dp[i - 1][j][:D - C[i][j]]
            x[:D - C[i][j]] |= dp[i - 1][j][C[i][j]:]
        if j != 0:
            x[C[i][j]:] |= dp[i][j - 1][:D - C[i][j]]
            x[:D - C[i][j]] |= dp[i][j - 1][C[i][j]:]
        dp[i][j] = x
temp = np.where(dp[-1][-1] > 0)[0] - d
temp = abs(temp)
print(min(temp))
