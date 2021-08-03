import numpy as np
N, K, *XYC = open(0).read().split()
N = int(N)
K = int(K)
board = np.zeros((4 * K + 1, 4 * K + 1), dtype=np.int64)
for x, y, c in zip(XYC[::3], XYC[1::3], XYC[2::3]):
    x = int(x)
    y = int(y)
    if c == 'W':
        x += K
    x = x % (2 * K)
    y = y % (2 * K)
    board[x, y] += 1
    board[(x + K) % (2 * K), (y + K) % (2 * K)] += 1
board[1 + 2 * K:, 1 + 2 * K:] = board[:2 * K, :2 * K]
board[1:1 + 2 * K, 1 + 2 * K:] = board[1 + 2 * K:, 1 + 2 * K:]
board[1 + 2 * K:, 1:1 + 2 * K] = board[1 + 2 * K:, 1 + 2 * K:]
board[1:1 + 2 * K, 1:1 + 2 * K] = board[1 + 2 * K:, 1 + 2 * K:]
board[0, :] = 0
board[:, 0] = 0
for j in range(1, 3 * K):
    board[:, j] += board[:, j - 1]
for j in range(1, 3 * K):
    board[j, :] += board[j - 1, :]
ans = np.max(board[K:3 * K, K:3 * K] + board[:2 * K, :2 * K]
             - board[:2 * K, K:3 * K] - board[K:3 * K, :2 * K])
print(ans)
