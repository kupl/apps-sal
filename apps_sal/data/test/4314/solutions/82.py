H, W = map(int,input().split())
A = [input() for i in range(H)]
row = [False]*H
col = [False]*W
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            row[i] = True
            col[j] = True
for i in range(H):
    if row[i]:
        for j in range(W):
            if col[j]:
                print(A[i][j], end = '')
        print()
