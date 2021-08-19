import numpy as np
(N, K) = map(int, input().split())
_3K = 3 * K
_2K = 2 * K
G = np.zeros((_2K, _3K), dtype='int64')
for _ in range(N):
    (x, y, c) = input().split()
    (x, y) = (int(x), int(y))
    if c == 'B':
        x = x % _2K
        y = y % _2K
    else:
        x = (x + K) % _2K
        y = y % _2K
    if y >= K and x >= K:
        x -= K
        y -= K
    if y >= K and x < K:
        x += K
        y -= K
    G[y, x] += 1
    G[y + K, x + K] += 1
    G[y + K, x] -= 1
    G[y, x + K] -= 1
G = G.cumsum(axis=1).cumsum(axis=0)
G = G[:K, :_2K] + G[K:_2K, K:_3K] + np.concatenate((G[:K, _2K:_3K], G[K:_2K, :K]), axis=1)
ans = G.max()
print(ans)
