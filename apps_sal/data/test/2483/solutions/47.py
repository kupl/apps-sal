import sys
import numpy as np
readline = sys.stdin.readline
read = sys.stdin.read
(n, c, *stc) = list(map(int, read().split()))
m = 2 * 10 ** 5
cht = np.zeros((c, m + 1), dtype='int64')
for (s, t, ch) in zip(*[iter(stc)] * 3):
    cht[ch - 1, 2 * s - 1:2 * t] = np.ones(2 * t - 2 * s + 1)
print(max(np.sum(cht, axis=0)))
