import sys
input = sys.stdin.readline

h,w=list(map(int,input().split()))
R=list(map(int,input().split()))
C=list(map(int,input().split()))

mod=10**9+7

ANS=[[0]*w for i in range(h)]

for i in range(h):
    for j in range(R[i]):
        ANS[i][j]=1

    if R[i]!=w:
        ANS[i][R[i]]=2

#print(ANS)

for i in range(w):
    for j in range(C[i]):
        if ANS[j][i]==2:
            print(0)
            return
        ANS[j][i]=1

    if C[i]!=h:
        if ANS[C[i]][i]==1:
            print(0)
            return
            
        ANS[C[i]][i]=2

count=0
for i in range(h):
    for j in range(w):
        if ANS[i][j]==0:
            count+=1

print(pow(2,count,mod))

