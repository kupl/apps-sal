import numpy as np
(h, w) = map(int, input().split())
s = [input() for _ in range(h)]
t = np.zeros((h, w), dtype=np.int32)
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            t[i][j] = 1
l = np.zeros((h, w), dtype=np.int32)
r = np.zeros((h, w), dtype=np.int32)
u = np.zeros((h, w), dtype=np.int32)
d = np.zeros((h, w), dtype=np.int32)
for i in range(w):
    if i == 0:
        l[:, i] = t[:, i]
    else:
        l[:, i] = (l[:, i - 1] + 1) * t[:, i]
for i in range(w - 1, -1, -1):
    if i == w - 1:
        r[:, i] = t[:, i]
    else:
        r[:, i] = (r[:, i + 1] + 1) * t[:, i]
for i in range(h):
    if i == 0:
        u[i] = t[i]
    else:
        u[i] = (u[i - 1] + 1) * t[i]
for i in range(h - 1, -1, -1):
    if i == h - 1:
        d[i] = t[i]
    else:
        d[i] = (d[i + 1] + 1) * t[i]
lrud = l + r + u + d - 3
print(np.max(lrud))
