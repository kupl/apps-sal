import sys

sys.setrecursionlimit(10**6)


N=int(input())
G=[[] for _ in range(N)]
for i in range(N-1):
    a,b,c=list(map(int,input().split()))
    G[a-1].append([b-1,c])
    G[b-1].append([a-1,c])

Q,K=list(map(int,input().split()))

SD=[0]*N
def DFS(v,p,d):
    SD[v]=d
    for i,co in G[v]:
        if i==p:continue
        DFS(i,v,d+co)
    return

DFS(K-1,-1,0)

for i in range(Q):
    x,y=list(map(int,input().split()))
    ans=SD[x-1]+SD[y-1]
    print(ans)


