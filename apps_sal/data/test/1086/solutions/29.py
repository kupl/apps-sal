import numpy as np
h, w = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(h)]
B = [list(map(int, input().split())) for i in range(h)]

C = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        C[i][j] = abs(A[i][j] - B[i][j])

dp = [[0] * (w + 1) for _ in range(h + 1)]
d = 80 * (h + w - 1) + 1
D = 2 * d + 1
dp[0][0] = np.zeros(D, np.bool)
dp[0][0][C[0][0] + d] = 1
for i in range(h):
    for j in range(w):
        c = C[i][j]
        if i == 0 and j == 0:
            continue
        elif i == 0:
            b = np.zeros(D, np.bool)
            b[c:] |= dp[i][j - 1][:D - c]
            b[:D - c] |= dp[i][j - 1][c:]
        elif j == 0:
            b = np.zeros(D, np.bool)
            b[c:] |= dp[i - 1][j][:D - c]
            b[:D - c] |= dp[i - 1][j][c:]
        else:
            b = np.zeros(D, np.bool)
            b[c:] |= dp[i][j - 1][:D - c]
            b[:D - c] |= dp[i][j - 1][c:]
            b[c:] |= dp[i - 1][j][:D - c]
            b[:D - c] |= dp[i - 1][j][c:]
        dp[i][j] = b
ans = float('inf')
for i in range(D):
    if dp[h - 1][w - 1][i]:
        ans = min(ans, abs(i - d))
print(ans)
