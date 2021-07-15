import sys
input = sys.stdin.readline
from collections import Counter

N=int(input())
E=[[] for i in range(N)]
for i in range(N-1):
    x,y=map(int,input().split())
    x-=1
    y-=1
    E[x].append(y)
    E[y].append(x)

mod=10**9+7

def dfs(x):
    DIS=[-1]*N
    DIS[x]=0
    Q=[x]

    while Q:
        x=Q.pop()
        for to in E[x]:
            if DIS[to]==-1:
                DIS[to]=DIS[x]+1
                Q.append(to)
    return DIS

D0=dfs(0)
L=D0.index(max(D0))
DL=dfs(L)
R=DL.index(max(DL))
DR=dfs(R)

MIN=[min(DL[i],DR[i]) for i in range(N)]
MAX=[max(DL[i],DR[i]) for i in range(N)]
C=Counter(MIN)

half=pow(2,mod-2,mod)%mod
ALL=pow(2,N,mod)
ANS=max(DR)*ALL*half%mod

MAX.sort()

dind=0
ANS=(ANS+max(MIN)*ALL*half)%mod

for d in range(max(MIN)+1,max(DR)+1):
    while dind<N and MAX[dind]<d:
        dind+=1
    ANS=(ANS+2*(ALL*half*half-pow(2,dind,mod)))%mod

print(ANS)
