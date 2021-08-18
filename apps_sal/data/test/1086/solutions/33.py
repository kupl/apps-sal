import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W = lr()
A = np.array([lr() for _ in range(H)])
B = np.array([lr() for _ in range(H)])
diff = np.abs(A - B).tolist()

X = (H + W) * 80
L = X + X + 1
dp = [[np.zeros(L, np.bool) for _ in range(W)] for _ in range(H)]
di = diff[0][0]
dp[0][0][X + di] = 1
dp[0][0][X - di] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        di = diff[i][j]
        if i > 0:
            prev = dp[i - 1][j]
            dp[i][j][di:] |= prev[:L - di]
            dp[i][j][:L - di] |= prev[di:]
        if j > 0:
            prev = dp[i][j - 1]
            dp[i][j][di:] |= prev[:L - di]
            dp[i][j][:L - di] |= prev[di:]

dp = dp[-1][-1][X:]
possible = np.nonzero(dp)[0]
answer = possible.min()
print(answer)
