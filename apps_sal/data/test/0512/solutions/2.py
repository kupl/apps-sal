N=int(input())
A=[0 for i in range(N)]
B=[0 for i in range(N)]
used=[0 for i in range(2*N)]
com=[-1 for i in range(2*N)]
for i in range(N):
    A[i],B[i]=list(map(int,input().split()))
    if A[i]!=-1:
        A[i]-=1
        if used[A[i]]:
            print("No")
            return
        used[A[i]]=i+1
    if B[i]!=-1:
        B[i]-=1
        if used[B[i]]:
            print("No")
            return
        used[B[i]]=-(i+1)
    if A[i]!=-1 and B[i]!=-1:
        if A[i]>B[i]:
            print("No")
            return
        com[A[i]]=B[i]
        com[B[i]]=A[i]
dp=[False for i in range(2*N+1)]
dp[0]=True
for i in range(2*N):
    if not(dp[i]):continue
    for j in range(i+1,2*N,2):
        w=(j-i+1)//2
        ok=True
        for k in range(w):
            p=i+k
            q=i+k+w
            if com[p]!=-1 and com[p]!=q:
                ok=False
            if com[q]!=-1 and com[q]!=p:
                ok=False
            if used[p]!=0 and used[q]!=0 and used[p]+used[q]!=0:
                ok=False
            if used[p]<0 or used[q]>0:
                ok=False
        if ok:
            dp[j+1]=True
if dp[2*N]:
    print("Yes")
else:
    print("No")

