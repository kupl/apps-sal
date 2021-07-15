import sys
sys.setrecursionlimit(10**6)# 各頂点ごとに所属する木の大きさを計算する
N,Q = list(map(int,input().split()))

E = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
Node_len = [1 for _ in range(N+1)]

for i in range(N-1):
    a,b = list(map(int,input().split()))
    E[a].append(b)
    E[b].append(a)

AS = [0 for i in range(N+1)]
def dfs(node,parent=-1):
    for child in E[node]:
        if child == parent:
            continue
        AS[child] += AS[node]
        dfs(child,node)

for q in range(Q):
    p,x = list(map(int,input().split()))
    AS[p] += x

dfs(1)
print((*AS[1:]))



