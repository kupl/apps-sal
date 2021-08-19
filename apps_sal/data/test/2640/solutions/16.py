import numpy as np
(h, w) = list(map(int, input().split()))
s = np.empty((h, w), dtype='i8')
for i in range(h):
    s[i] = [i == '.' for i in list(input())]
right = np.copy(s)
left = np.copy(s)
for i in range(1, w):
    right[:, -i - 1] = (right[:, -i] + 1) * s[:, -i - 1]
    left[:, i] = (left[:, i - 1] + 1) * s[:, i]
up = np.copy(s)
down = np.copy(s)
for i in range(1, h):
    up[i] = (up[i - 1] + 1) * s[i]
    down[-i - 1] = (down[-i] + 1) * s[-i - 1]
print(np.max(right + left + up + down) - 3)
