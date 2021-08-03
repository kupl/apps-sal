import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W = lr()
A = [lr() for _ in range(H)]
B = [lr() for _ in range(H)]
diff = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        diff[i][j] = abs(A[i][j] - B[i][j])

X = (H + W) * 80
L = X + X + 1  # 真ん中を0とする、最後に-X
dp = [[None] * W for _ in range(H)]
dp[0][0] = np.zeros(L, np.bool)
dp[0][0][X + diff[0][0]] = 1
dp[0][0][X - diff[0][0]] = 1  # 非負整数のみでも良い
for h in range(H):
    for w, di in enumerate(diff[h]):
        if h == 0 and w == 0:
            continue
        x = np.zeros(L, np.bool)
        if h > 0:
            x[di:] |= dp[h - 1][w][:L - di]
            x[:L - di] |= dp[h - 1][w][di:]
        if w > 0:
            x[di:] |= dp[h][w - 1][:L - di]
            x[:L - di] |= dp[h][w - 1][di:]
        dp[h][w] = x

dp = dp[-1][-1]
possible = np.where(dp)[0] - X
answer = np.abs(possible).min()
print(answer)
# 07
