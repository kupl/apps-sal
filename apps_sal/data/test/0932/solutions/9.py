(m, n) = list(map(int, input().split(' ')))
B = []
for i in range(0, m):
    row = [int(x) for x in input().split(' ')]
    B.append(row)

B_ = []
for j in range(0, n):
    col = [B[i][j] for i in range(0, m)]
    B_.append(col)

for row in B:
    if 1 in row:
        if 0 in row:
            for j in range(0, n):
                col = [B[i][j] for i in range(0, m)]
                if (row[j] == 1 and 0 in col):
                    print("NO")
                    return

for col in B_:
    if 1 in col:
        if 0 in col:
            for i in range(0, m):
                row = [B[i][j] for j in range(0, n)]
                if (col[i] == 1 and 0 in row):
                    print("NO")
                    return

only1 = False
only0 = False
for row in B:
    if 1 not in row:
        only0 = True
    if 0 not in row:
        only1 = True
if only1 and only0:
    print("NO")
    return

only1 = False
only0 = False
for col in B_:
    if 1 not in col:
        only0 = True
    if 0 not in col:
        only1 = True
if only1 and only0:
    print("NO")
    return

A = [[0 for col in range(0, n)] for row in range(0, m)]
R = []
for i in range(0, m):
    flg = 1
    for j in range(0, n):
        if B[i][j] == 0:
            flg = 0
            break
    if flg == 1:
        R.append(i)
C = []
for j in range(0, n):
    flg = 1
    for i in range(0, m):
        if B[i][j] == 0:
            flg = 0
            break
    if flg == 1:
        C.append(j)

for r in R:
    for c in C:
        A[r][c] = 1

print("YES")
for i in range(0, m):
    s = "" + str(A[i][0])
    for j in range(1, n):
        s += " " + str(A[i][j])
    print(s)
