import numpy as np
H, W = map(int, input().split())
mat = []
for h in range(H):
    row = []
    A = list(input())
    for a in A:
        if a == '.':
            row.append(0)
        elif a == '
            row.append('
    mat.append(row)

for i in range(H):
    for j in range(W):
        if mat[i][j] != '
            for h, w in zip([0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]):
                if i + h >= 0 and i + h < H and j + w >= 0 and j + w < W:
                    if mat[i + h][j + w] == '
                        mat[i][j] += 1
for i in mat:
    print(*i, sep='')
