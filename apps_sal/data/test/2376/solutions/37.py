import numpy as np
(N, W) = list(map(int, input().split()))
ls = []
for i in range(N):
    (w, v) = list(map(int, input().split()))
    ls += [[w, v]]
ls = np.array(ls)
w1 = ls[0][0]
ls[:, 0] -= w1
M = 3 * N
dp = np.full((N + 1, M + 1), -float('inf'))
dp[0][0] = 0
for i in range(N):
    (w, v) = ls[i]
    dp[1:, w:] = np.maximum(dp[1:, w:], dp[:N, :M - w + 1] + v)
ans = 0
for i in range(1, N + 1):
    B = i * w1
    m = 0
    for j in range(M + 1):
        if B + j <= W:
            m = max(m, dp[i][j])
    if ans < m:
        ans = m
print(int(ans))
