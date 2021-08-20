import numpy as np
(N, K) = map(int, input().split())
(_2K, _4K) = (2 * K, 4 * K)
shape = (_2K + 1, _4K + 1)
Grd = np.zeros(shape, dtype='int64')
for _ in range(N):
    (x, y, c) = input().split()
    (x, y) = (int(x), int(y))
    if c == 'B':
        (x, y) = (x % _2K, y % _2K)
    else:
        (x, y) = ((x + K) % _2K, y % _2K)
    if x >= K and y >= K:
        x -= K
        y -= K
    if x < K and y >= K:
        x += K
        y -= K
    Grd[y, x] += 1
    Grd[y + K, x + K] += 1
    Grd[y + K, x] += -1
    Grd[y, x + K] += -1
del x, y, c
Grd = Grd.cumsum(axis=1).cumsum(axis=0)
Grd = Grd[:, :_2K] + Grd[:, _2K:_4K]
Grd = Grd[:K, :] + np.concatenate((Grd[K:_2K, K:_2K], Grd[K:_2K, :K]), axis=1)
ans = Grd.max()
print(ans)
