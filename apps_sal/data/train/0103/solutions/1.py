q = int(input())
for _ in range(q):
    r,c = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(r)]
    row = 0
    for i in mat:
        if sum(i) == 0:
            row += 1
    col = 0
    for i in range(c):
        su = 0
        for j in range(r):
            su += mat[j][i]
        if su == 0:
            col += 1
    cyk = min(row, col)
    if cyk%2 == 0:
        print("Vivek")
    else:
        print("Ashish")
