mod=10**9+7

N,M=map(int,input().split())
L=-1;R=-1
S=input()
ope=[]
for i in range(M):
    l,r=map(int,input().split())
    l-=1;r-=1
    if L<=l and r<=R:
        continue
    else:
        L,R=l,r
        ope.append((l,r))

M=len(ope)
data=[-1]*N
for i in range(M):
    l,r=ope[i]
    for j in range(l,r+1):
        data[j]=i

dp=[[0 for i in range(N+1)] for j in range(N+1)]

for j in range(N+1):
    dp[-1][j]=1

for i in range(N-1,-1,-1):
    id=data[i]
    if id!=-1:
        l,r=ope[id]
        temp1=sum(int(S[k]) for k in range(r+1))
        temp0=r+1-temp1
        for j in range(temp1+1):
            np1=temp1-j
            np0=temp0-(i-j)
            if np1==0:
                if np0>0:
                    dp[i][j]=dp[i+1][j]
            else:
                if np0>0:
                    dp[i][j]=(dp[i+1][j+1]+dp[i+1][j])%mod
                elif np0==0:
                    dp[i][j]=dp[i+1][j+1]
    else:
        if S[i]=="1":
            for j in range(N):
                dp[i][j]=dp[i+1][j+1]
        else:
            for j in range(N+1):
                dp[i][j]=dp[i+1][j]

print(dp[0][0])
