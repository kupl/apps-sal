import numpy as np
(h, w) = list(map(int, input().split()))
s = np.array([list(input()) for _ in range(h)]) == '.'
ups = np.zeros((h, w), dtype=int)
downs = np.zeros((h, w), dtype=int)
rights = np.zeros((h, w), dtype=int)
lefts = np.zeros((h, w), dtype=int)
for i in range(1, h):
    ups[i, :] = (ups[i - 1] + 1) * s[i - 1]
for i in reversed(list(range(h - 1))):
    downs[i, :] = (downs[i + 1] + 1) * s[i + 1]
for i in range(1, w):
    rights[:, i] = (rights[:, i - 1] + 1) * s[:, i - 1]
for i in reversed(list(range(w - 1))):
    lefts[:, i] = (lefts[:, i + 1] + 1) * s[:, i + 1]
ans = ((ups + downs + lefts + rights) * s).max() + 1
print(ans)
