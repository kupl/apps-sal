(H, W) = map(int, input().split())
A = [''] * H
for i in range(H):
    A[i] = input()
row = [False] * H
col = [False] * W
for j in range(H):
    for k in range(W):
        if A[j][k] == '#':
            row[j] = True
            col[k] = True
for l in range(H):
    if row[l]:
        for m in range(W):
            if col[m]:
                print(A[l][m], end='')
        print()
