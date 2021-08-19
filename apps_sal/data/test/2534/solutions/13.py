(n, m) = map(int, input().strip().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().strip().split())))


def rmin(mat, r):
    row = mat[r]
    rm = min(row)
    return rm


def cmax(mat, c):
    col = list((_[c] for _ in mat))
    cm = max(col)
    return cm


rm = list((rmin(mat, _) for _ in range(n)))
cm = list((cmax(mat, _) for _ in range(m)))
num = 0
for _ in range(n):
    for __ in range(m):
        if mat[_][__] == rm[_]:
            if mat[_][__] == cm[__]:
                num = mat[_][__]
                break
    if num != 0:
        break
if num != 0:
    print(num)
else:
    print('GUESS')
