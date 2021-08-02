import numpy as np
H, W = map(int, input().split(' '))
maze = [list(input()) for i in range(H)]
maze = (np.array(maze) == '.') * 1
L = np.zeros((H, W), dtype=int)
R = np.zeros((H, W), dtype=int)
U = np.zeros((H, W), dtype=int)
D = np.zeros((H, W), dtype=int)
for i in range(W):
    if i == 0:
        L[:, i] = maze[:, i]
        R[:, W - i - 1] = maze[:, W - i - 1]
    else:
        L[:, i] = (L[:, i - 1] + 1) * maze[:, i]
        R[:, W - i - 1] = (R[:, W - i] + 1) * maze[:, W - i - 1]
for i in range(H):
    if i == 0:
        U[i, :] = maze[i, :]
        D[H - i - 1, :] = maze[H - i - 1, :]
    else:
        U[i, :] = (U[i - 1, :] + 1) * maze[i, :]
        D[H - i - 1, :] = (D[H - i] + 1) * maze[H - i - 1, :]
print(max(np.max(U + D + L + R - 3), 0))
