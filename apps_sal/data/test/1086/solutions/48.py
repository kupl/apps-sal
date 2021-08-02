import numpy as np

h, w = map(int, input().split())
A = [0] * h
B = [0] * h
for _ in range(h):
    A[_] = list(map(int, input().split()))

for _ in range(h):
    B[_] = list(map(int, input().split()))

C = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        C[i][j] = abs(A[i][j] - B[i][j])

dp = [[0] * w for _ in range(h)]
D = 80 * (h + w)
L = 2 * D + 1
dp[0][0] = np.zeros(L, np.bool)
dp[0][0][D + C[0][0]] = 1
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        x = np.zeros(L, np.bool)
        if i != 0:
            x[C[i][j]:] |= dp[i - 1][j][:L - C[i][j]]
            x[:L - C[i][j]] |= dp[i - 1][j][C[i][j]:]
        if j != 0:
            x[C[i][j]:] |= dp[i][j - 1][:L - C[i][j]]
            x[:L - C[i][j]] |= dp[i][j - 1][C[i][j]:]
        dp[i][j] = x

temp = np.where(dp[-1][-1] > 0)[0] - D
temp = np.abs(temp)
print(np.min(temp))
