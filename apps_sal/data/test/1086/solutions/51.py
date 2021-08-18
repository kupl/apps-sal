import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W = lr()
A = np.array([lr() for _ in range(H)])
B = np.array([lr() for _ in range(H)])
diff = np.abs(A - B)

X = (H + W) * 80
L = X + X + 1
dp = [[None] * W for _ in range(H)]
dp[0][0] = np.zeros(L, np.bool)
dp[0][0][X + diff[0][0]] = 1
dp[0][0][X - diff[0][0]] = 1
for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            continue
        di = diff[h][w]
        x = np.zeros(L, np.bool)
        if h > 0:
            x[di:] |= dp[h - 1][w][:L - di]
            x[:L - di] |= dp[h - 1][w][di:]
        if w > 0:
            x[di:] |= dp[h][w - 1][:L - di]
            x[:L - di] |= dp[h][w - 1][di:]
        dp[h][w] = x

dp = dp[-1][-1][X:]
possible = np.where(dp == 1)[0]
answer = possible.min()
print(answer)
