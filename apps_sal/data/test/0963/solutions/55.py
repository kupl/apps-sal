n,k=map(int,input().split())
S=[]
for i in range(k):
    s=list(map(int,input().split()))
    S.append(s)
mod=998244353
DP=[0 for i in range(n+1)]
DP[1]=1
R=[0 for i in range(n+1)]
R[1]=1
for i in range(2,n+1):
    for l,r in S:
        li=i-r
        ri=i-l
        if ri<0:
            continue
        DP[i]+=R[ri]-R[max(li-1,0)]
        DP[i]%=mod
    R[i]=R[i-1]+DP[i]
    R[i]%=mod
print(DP[n])
