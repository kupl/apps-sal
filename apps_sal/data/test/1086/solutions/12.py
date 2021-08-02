import sys
import numpy as np
input = sys.stdin.readline
h, w = [int(j) for j in input().split()]
a = []
b = []
a = [[int(j) for j in input().split()] for i in range(h)]
b = [[int(j) for j in input().split()] for i in range(h)]
x = (h + w) * 80
l = 2 * x + 1
dp = [[0] * w for i in range(h)]
dp[0][0] = np.zeros(l, np.bool)
d = abs(a[0][0] - b[0][0])
dp[0][0][x + d] = 1
for i in range(h):
    for j, (s, t) in enumerate(zip(a[i], b[i])):
        if i == j == 0:
            continue
        d = abs(s - t)
        p = np.zeros(l, np.bool)
        if i != 0:
            p[d:] |= dp[i - 1][j][:l - d]
            p[:l - d] |= dp[i - 1][j][d:]
        if j != 0:
            p[d:] |= dp[i][j - 1][:l - d]
            p[:l - d] |= dp[i][j - 1][d:]
        dp[i][j] = p

ans = np.abs(np.where(dp[-1][-1])[0] - x).min()
print(ans)
