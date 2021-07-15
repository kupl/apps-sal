H,W = list(map(int,input().split()))
L = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if L[i][j] == '#':
            if i != 0 and L[i-1][j] == '#':
                continue
            if i != H-1 and L[i+1][j] == '#':
                continue
            if j != 0 and L[i][j-1] == '#':
                continue
            if j != W-1 and L[i][j+1] == '#':
                continue
            print('No')
            return
print('Yes')

