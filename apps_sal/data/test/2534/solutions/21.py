(r, c) = map(int, input().split())
mat = []
for i in range(r):
    mat.append(list(map(int, input().split())))
flag = 0
for i in range(r):
    min = 10000000000000
    col = []
    for j in range(c):
        if mat[i][j] < min:
            min = mat[i][j]
    for j in range(c):
        if mat[i][j] == min:
            col.append(j)
    for m in col:
        max = 0
        for k in range(r):
            if mat[k][m] > max:
                max = mat[k][m]
        if max == min:
            flag = 1
            print(max)
            break
    if flag == 1:
        break
if flag == 0:
    print('GUESS')
