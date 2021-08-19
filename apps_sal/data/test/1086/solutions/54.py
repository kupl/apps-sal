import numpy as np
import itertools
(H, W) = list(map(int, input().split()))
A = [tuple(map(int, input().split())) for _ in range(H)]
B = [tuple(map(int, input().split())) for _ in range(H)]
D = [[abs(A[h][w] - B[h][w]) for w in range(W)] for h in range(H)]
max_num = 80 * (H + W)
table = np.zeros((H, W, max_num), dtype='bool')
table[0][0][D[0][0]] = True
it = itertools.product(list(range(H)), list(range(W)))
next(it)
for (h, w) in it:
    d = D[h][w]
    table[h][w][d:] += table[h - 1][w][:max_num - d] + table[h][w - 1][:max_num - d]
    table[h][w][:max_num - d] += table[h - 1][w][d:] + table[h][w - 1][d:]
    table[h][w][d:0:-1] += table[h - 1][w][:d] + table[h][w - 1][:d]
print(np.amin(*np.where(table[H - 1][W - 1])))
