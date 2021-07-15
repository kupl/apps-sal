H,W = map(int,input().split())
HW = [[0]*(W+1)]+[[0]+list(map(int,input().split())) for i in range(H)]
f = 0
rev = False
lsmove = []
N = 0
i = 1
while i <= H:
    if rev == False:
        for j in range(1,W+1):
            if HW[i][j] % 2 == 0:
                continue
            else:
                if j != W:
                    lsmove.append([i,j,i,j+1])
                    HW[i][j+1] += 1
                    N += 1
                elif i != H:
                    lsmove.append([i,j,i+1,j])
                    HW[i+1][j] += 1
                    N += 1
        rev = True
        i += 1
        if j == W and i == H+1:
            break
    if rev == True:
        for j in range(W,0,-1):
            if HW[i][j] % 2 == 0:
                continue
            else:
                if j != 1:
                    lsmove.append([i,j,i,j-1])
                    HW[i][j-1] += 1
                    N += 1
                elif i != H:
                    lsmove.append([i,j,i+1,j])
                    HW[i+1][j] += 1
                    N += 1
        rev = False
        i += 1
        if j == 1 and i == H+1:
            break
print(N)
for i in lsmove:
    print(*i,sep=(' '))
