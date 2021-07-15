n,k0=map(int,input().split())
mod=10**9+7

# DP[j,k]=l で,j個保留してスコアkのときの場合の数がl

from collections import defaultdict

DP=defaultdict(int)
DP[0,0]=1

for i in range(n):
    NDP=defaultdict(int)

    for j,k in DP:
        l=DP[j,k]

        NDP[j,k+2*j]=(NDP[j,k+2*j]+l)%mod

        if j>=1:
            NDP[j,k+2*j]=(NDP[j,k+2*j]+2*j*l)%mod

        if j>=1:
            NDP[j-1,k+2*(j-1)]=(NDP[j-1,k+2*(j-1)]+j*j*l)%mod

        NDP[j+1,k+2*(j+1)]=(NDP[j+1,k+2*(j+1)]+l)%mod

    DP=NDP

ANS=0
for j,k in DP:
    if j==0 and k==k0:
        ANS+=DP[j,k]

print(ANS%mod)
