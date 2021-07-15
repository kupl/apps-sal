import sys
sys.setrecursionlimit(10**7)

n=int(input())

graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = list(map(int, input().split()))
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

q,k=list(map(int, input().split()))
k-=1

dist=[-1]*n

def dfs(now, parent, d):
    dist[now]=d
    for i in graph[now]:
        if i[0]==parent:
            continue
        else:
            dfs(i[0], now, d+i[1])

dfs(k, -1, 0)

for _ in range(q):
    x,y=list(map(int, input().split()))
    x-=1
    y-=1
    print((dist[x]+dist[y]))


