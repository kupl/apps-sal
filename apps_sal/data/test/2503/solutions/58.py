import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, K = lr()
table = [[0] * 2 * K for _ in range(K)]
for _ in range(N):
    x, y, c = sr().split()
    x = int(x)
    y = int(y)
    if c == 'B':
        x -= K
    x %= 2 * K
    y %= 2 * K
    if x >= K and y >= K:
        x -= K
        y -= K
    elif y >= K:
        x += K
        y -= K
    table[y][x] += 1

table = np.array(table, dtype=np.int32)
table = np.concatenate([table, table], axis=1)
table2 = np.roll(table, K, axis=1)
table = np.concatenate([table, table2], axis=0)
table_cum = table.cumsum(axis=1).cumsum(axis=0)
prev = table_cum.copy()
table_cum[:, K:] -= prev[:, :-K]
table_cum[K:, :] -= prev[:-K, :]
table_cum[K:, K:] += prev[:-K, :-K]
answer = table_cum.max()
print(answer)
