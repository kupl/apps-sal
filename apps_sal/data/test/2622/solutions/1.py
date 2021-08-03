n, m = list(map(int, input().strip().split(' ')))
mat1, mat2 = [], []
for i in range(0, n):
    mat1.append(tuple(input().strip()))
for i in range(0, m):
    mat2.append(tuple(input().strip()))
ix, jx, flg = -1, -1, 0
matr, matc = [], []
for i in range(0, n - m + 1):
    si, se = i, i + m
    matr.append(hash(tuple(mat1[si:se])))
    matcur2 = []
    for c2i in range(0, m):
        matcur2.append(tuple(mat2[c2i][si:se]))
    matc.append(hash(tuple(matcur2)))
nx = len(matr)
ix, jx = -1, -1
for ix in range(0, nx):
    flg = 0
    for jx in range(0, nx):
        if matr[ix] == matc[jx]:
            flg = 1
            break
    if flg == 1:
        break
print(str(ix + 1) + " " + str(jx + 1))
