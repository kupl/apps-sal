import numpy as np
import io

nime, mike = map(int, input().split())
mod = 2 * mike
array = [[0] * (2 * mike + 1) for _ in range(2 * mike + 1)]


def gen_pattern(x):
    if x < mike - 1:
        return [[0, x + 1], [x + mike + 1, 2 * mike]]
    else:
        return [[x - mike + 1, x + 1]]


for _ in range(nime):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == 'W':
        y += mike
    x %= mod
    y %= mod
    for tmp in [0, mike]:
        for l, r in gen_pattern((x + tmp) % mod):
            for b, t in gen_pattern((y + tmp) % mod):
                array[l][b] += 1
                array[l][t] -= 1
                array[r][b] -= 1
                array[r][t] += 1
print(np.max(np.cumsum(np.cumsum(array, axis=0), axis=1)))
