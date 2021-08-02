import copy
n = int(input())
flg = 0
mat1 = []
mat2 = []

mats = []
for i in range(0, n):
    mat1.append(tuple(input().strip()))
for i in range(0, n):
    mat2.append(tuple(input().strip()))
mats.append(mat2)
matu = copy.copy(mat2)
matv = copy.copy(mat2)
matv = list(zip(*matv))
mats.append(matv)

mattem = copy.copy(matu)
for i in range(0, 3):
    mattem = list(zip(*list(reversed(mattem))))
    mats.append(mattem)
mattem = copy.copy(matv)
for i in range(0, 3):
    mattem = list(zip(*list(reversed(mattem))))
    mats.append(mattem)

flg = 0
for cmat in mats:
    flg2 = 1
    for ri in range(0, n):
        if cmat[ri] != mat1[ri]:
            flg2 = 0
            break
    if flg2 == 1:
        flg = 1
        break
if flg == 1:
    print("Yes")
else:
    print("No")
