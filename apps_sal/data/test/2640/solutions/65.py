import numpy as np
(h, w) = map(int, input().split())
S = np.array([list(input()) for _ in range(h)])
S = np.where(S == '.', 1, 0)
(left, right, up, down) = [np.zeros((h, w), dtype=np.int64) for _ in range(4)]
for i in range(w):
    left[:, i] = (left[:, i - 1] + 1) * S[:, i]
    right[:, -i - 1] = (right[:, -i] + 1) * S[:, -i - 1]
for i in range(h):
    up[i] = (up[i - 1] + 1) * S[i]
    down[-i - 1] = (down[-i] + 1) * S[-i - 1]
print(int(np.max(left + right + up + down) - 3))
