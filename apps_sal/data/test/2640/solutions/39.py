import numpy as np
(h, w) = map(int, input().split())
s = [list(input()) for i in range(h)]
s = np.array(s)
s = np.where(s == '.', 1, 0)
L = np.zeros((h, w), dtype=np.int)
R = np.zeros((h, w), dtype=np.int)
U = np.zeros((h, w), dtype=np.int)
D = np.zeros((h, w), dtype=np.int)
for i in range(w):
    L[:, i] = (L[:, i - 1] + 1) * s[:, i]
    R[:, -i - 1] = (R[:, -i] + 1) * s[:, -i - 1]
for i in range(h):
    U[i] = (U[i - 1] + 1) * s[i]
    D[-i - 1] = (D[-i] + 1) * s[-i - 1]
ans = np.max(L + R + U + D) - 3
print(ans)
