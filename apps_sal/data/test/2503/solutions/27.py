import numpy as np
(N, K) = list(map(int, input().split()))
mod = 2 * K
field = [[0] * (2 * K + 1) for _ in range(2 * K + 1)]


def gen_pattern(x):
    if x < K - 1:
        return [[0, x + 1], [x + K + 1, 2 * K]]
    else:
        return [[x - K + 1, x + 1]]


for _ in range(N):
    (x, y, c) = input().split()
    (x, y) = (int(x), int(y))
    if c == 'W':
        y += K
    x %= mod
    y %= mod
    for tmp in [0, K]:
        for (l, r) in gen_pattern((x + tmp) % mod):
            for (b, t) in gen_pattern((y + tmp) % mod):
                field[l][b] += 1
                field[l][t] -= 1
                field[r][b] -= 1
                field[r][t] += 1
field = np.array(field)
print(field.cumsum(axis=0).cumsum(axis=1).max())
