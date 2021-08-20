import numpy as np
(h, w) = map(int, input().split())
g = np.array([list(input()) for _ in range(h)])
g = np.where(g == '.', 1, 0)
l = np.zeros((h, w), dtype=np.int)
r = np.zeros((h, w), dtype=np.int)
u = np.zeros((h, w), dtype=np.int)
d = np.zeros((h, w), dtype=np.int)
for i in range(w):
    l[:, i] = (l[:, i - 1] + 1) * g[:, i]
    r[:, -i - 1] = (r[:, -i] + 1) * g[:, -i - 1]
for i in range(h):
    u[i, :] = (u[i - 1, :] + 1) * g[i, :]
    d[-i - 1, :] = (d[-i, :] + 1) * g[-i - 1, :]
print(np.max(l + r + u + d) - 3)
