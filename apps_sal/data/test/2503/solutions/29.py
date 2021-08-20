import numpy as np
(n, k) = map(int, input().split())
m = np.zeros((3 * k, 3 * k), dtype=int)
l = 2 * k
o = 0
for _ in range(n):
    (x, y, c) = input().split()
    (x, y) = (int(x) % l, int(y) % l)
    t = c == 'W'
    m[x, y] += 1 - 2 * t
    o += t
for _ in range(2):
    m[l:] = m[:k]
    m = np.cumsum(m, axis=0)
    m[:l] = m[k:] - m[:l]
    m = m.T
m = m[:l, :l]
print(o + (m + np.roll(np.roll(m, k, axis=0), k, axis=1)).max())
