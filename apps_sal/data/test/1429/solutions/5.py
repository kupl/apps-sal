# 各区画Tが自分自身を並べ替えた文字列と相補的であるかどうかを調べていく。

n,s=input().split()
N=int(n)
S=list(s)
A=[0 for _ in range(N)]
G=[0 for _ in range(N)]
C=[0 for _ in range(N)]
T=[0 for _ in range(N)]

for i in range(N):
    if S[i]=="A":
        A[i]=1
    elif S[i]=="G":
        G[i]=1
    elif S[i]=="C":
        C[i]=1
    elif S[i]=="T":
        T[i]=1


ans=0
for i in range(N):
    Asum=0
    Gsum=0
    Tsum=0
    Csum=0
    for j in range(i,N):
        Asum+=A[j]
        Gsum+=G[j]
        Csum+=C[j]
        Tsum+=T[j]
        if Asum==Tsum and Csum==Gsum:
            ans+=1

print(ans)


