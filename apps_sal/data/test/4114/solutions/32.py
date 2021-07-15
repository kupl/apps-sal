import sys
N = int(input())
ls = []
for i in range(N):
    x,y,h = map(int,input().split())
    ls.append([x,y,h])
ls.sort(key=lambda x: -x[2])

for i in range(0,101):
    for j in range(0,101):
        f = True
        H = ls[0][2]+abs(i-ls[0][0])+abs(j-ls[0][1])
        for k in range(1,N):
            if ls[k][2] != 0:
                H1 = ls[k][2]+abs(i-ls[k][0])+abs(j-ls[k][1])
                if H1 != H:
                    f = False
                    break
            else:
                if H > abs(i-ls[k][0])+abs(j-ls[k][1]):
                    f = False
                    break
        if f:
            print(i,j,H)
            return
