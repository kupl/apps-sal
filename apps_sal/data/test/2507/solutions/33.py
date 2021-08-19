import numpy as np
(n, k) = map(int, input().split())
a = np.array(input().split(), dtype=np.int64)
f = np.array(input().split(), dtype=np.int64)
a.sort()
f.sort()
f = f[::-1]
af = a * f


def safe(r):
    return np.maximum(0, (af - r + f - 1) // f).sum() <= k


m = -1
M = 10 ** 12
while m + 1 < M:
    pos = (m + M) // 2
    if safe(pos):
        M = pos
    else:
        m = pos
print(M)
