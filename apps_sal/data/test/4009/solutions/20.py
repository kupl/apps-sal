n,x,y=list(map(int,input().split()))
A=input()[-x:]
B=str(10**y).zfill(x)

ANS=0
for i in range(x):
    if A[i]!=B[i]:
        ANS+=1

print(ANS)

