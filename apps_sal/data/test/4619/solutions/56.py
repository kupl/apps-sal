import numpy as np
(w, h, n) = map(int, input().split())
loc = [input() for _ in range(n)]


def black(x, y, i):
    if i == 1:
        mtx[:x, ] = 0
    elif i == 2:
        mtx[x:, ] = 0
    elif i == 3:
        mtx[:, :y] = 0
    elif i == 4:
        mtx[:, y:] = 0


mtx = np.ones((w, h), dtype=int)
for l in loc:
    (x, y, i) = map(int, l.split())
    black(x, y, i)
print(mtx.sum())
