# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 縦K、横2*Kの長方形に全ての希望をWとして入れる
# numpyの累積和、最後にmaxをとる
N, K = lr()
table = [[0] * 2 * K for _ in range(K)]
for _ in range(N):
    x, y, c = sr().split()
    x = int(x); y = int(y)
    if c == 'B':
        x -= K  # ここで全てWとして扱える
    x %= 2 * K; y %= 2 * K
    if x >= K and y >= K:
        x -= K; y -= K
    elif y >= K:
        x += K; y -= K
    # 長方形に入った
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
