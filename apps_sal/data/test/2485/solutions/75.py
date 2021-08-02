import numpy as np
H, W, M = map(int, input().split())
col = np.zeros(H)
row = np.zeros(W)
memo = []
for i in range(M):
    h, w = map(int, input().split())
    h -= 1
    w -= 1
    col[h] += 1
    row[w] += 1
    memo.append((h, w))

col_max = col.max()
row_max = row.max()

col_max_indexes = np.where(col == col_max)[0]
row_max_indexes = np.where(row == row_max)[0]

ans = col_max + row_max - 1
memo = set(memo)
for c in col_max_indexes:
    for r in row_max_indexes:
        if (c, r) not in memo:
            ans = col_max + row_max
            print(int(ans))
            return

print(int(ans))
