from collections import deque
import math

n,m,p = map(int, input().split())
dist  = []
edge1 = [[] for _ in range(n)]
edge2 = [[] for _ in range(n)]  # rev_edge
for _ in range(m):
    u,v,c = map(int, input().split())
    u -= 1
    v -= 1
    dist.append((u,v,(c-p)*-1))
    edge1[u].append(v)
    edge2[v].append(u)   

def dfs(edges, s):
    stack = deque([s])
    used  = {s}
    while stack:
        x = stack.pop()
        for y in edges[x]:
            if y not in used:
                used.add(y)
                stack.append(y)
    return used


def bfs(edges, s):
    queue = deque([s])
    used  = {s}
    while queue:
        x = queue.popleft()
        for y in edges[x]:
            if y in used:
                continue
            used.add(y)
            queue.append(y)
    return used
    

def bellman(dist):  #負辺があるケースでの、スタートからゴールへの最短路を求めるアルゴ。
    cost = [float("inf")] * n
    cost[0] = 0
    for _ in range(n): #頂点の個数の分だけ回る
        updated = False
        for u,v,c in dist: #辺の個数の分だけ回る
            if cost[u] + c < cost[v]:
                cost[v] = cost[u] + c
                updated = True                
    #収束しない場合は負閉路があるため無限に小さくできる。
    if updated==True:
        return -1
    else:
        return max(0, cost[n-1]*-1)     
    
use = bfs(edge1, 0) & bfs(edge2, n-1)
dist2 = [(a,b,c) for a,b,c in dist if a in use and b in use]
print(bellman(dist2))
