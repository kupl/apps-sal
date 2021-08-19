import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(H, W) = lr()
A = np.array([lr() for _ in range(H)])
B = np.array([lr() for _ in range(H)])
diff = np.abs(A - B).tolist()
X = (H + W) * 80
L = X + X + 1
dp = [[None] * W for _ in range(H)]
dp[0][0] = np.zeros(L, np.bool)
di = diff[0][0]
dp[0][0][X + di] = 1
dp[0][0][X - di] = 1
for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            continue
        di = diff[h][w]
        x = np.zeros(L, np.bool)
        if h > 0:
            prev = dp[h - 1][w]
            x[di:] |= prev[:L - di]
            x[:L - di] |= prev[di:]
        if w > 0:
            prev = dp[h][w - 1]
            x[di:] |= prev[:L - di]
            x[:L - di] |= prev[di:]
        dp[h][w] = x
dp = dp[-1][-1][X:]
possible = np.nonzero(dp)[0]
answer = possible.min()
print(answer)
