N,A,B,C=map(int,input().split())
L=[int(input()) for i in range(N)]
R=[0]*N
ans=10**9
def myadd(i):
    if R[i]==3:
        R[i]=0
        myadd(i+1)
    else:
        R[i]+=1
for i in range(4**N-1):
    myadd(0)
    if 1 in R and 2 in R and 3 in R:
        tmp=-30
        t1,t2,t3=0,0,0
        for j in range(N):
            if R[j]==0:
                continue
            if R[j]==1:
                t1+=L[j]
            elif R[j]==2:
                t2+=L[j]
            elif R[j]==3:
                t3+=L[j]
            tmp+=10
        tmp+=abs(A-t1)+abs(B-t2)+abs(C-t3)
        ans=min(tmp,ans)
print(ans)
