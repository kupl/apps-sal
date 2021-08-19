# E71_B

ln = [int(i) for i in input().split(" ")]
n = ln[0]
m = ln[1]

mat = []
good = []
for i in range(0, n):
    mat.append([int(j) for j in input().split(" ")])
    good.append([0] * m)

seq = []

for i in range(0, n - 1):
    for j in range(0, m - 1):
        if mat[i][j] == 1 and mat[i + 1][j] == 1 and mat[i][j + 1] == 1 and mat[i + 1][j + 1] == 1:
            good[i][j] = True
            good[i + 1][j] = True
            good[i][j + 1] = True
            good[i + 1][j + 1] = True
            seq.append([i + 1, j + 1])

f = True

for i in range(0, n):
    for j in range(0, m):
        if mat[i][j] == 1 and not good[i][j]:
            f = False

if not f:
    print(-1)
elif len(seq) == 0:
    print(0)
else:
    print(len(seq))
    for i in seq:
        print(" ".join([str(j) for j in i]))
