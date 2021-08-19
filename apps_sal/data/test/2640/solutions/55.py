import numpy as np
(H, W) = map(int, input().split())
S = np.array([list(input()) for _ in range(H)])
S = np.where(S == '.', 1, 0)
left = np.zeros((H, W))
right = np.zeros((H, W))
top = np.zeros((H, W))
bottom = np.zeros((H, W))
for i in range(W):
    if i == 0:
        left[:, i] = S[:, i]
        right[:, -i - 1] = S[:, -i - 1]
    else:
        left[:, i] = (left[:, i - 1] + 1) * S[:, i]
        right[:, -i - 1] = (right[:, -i] + 1) * S[:, -i - 1]
for i in range(H):
    if i == 0:
        top[i, :] = S[i, :]
        bottom[-1 - i, :] = S[-i - 1, :]
    else:
        top[i, :] = (top[i - 1, :] + 1) * S[i, :]
        bottom[-1 - i, :] = (bottom[-i, :] + 1) * S[-i - 1, :]
ans = left + top + right + bottom - 3
print(int(ans.max()))
