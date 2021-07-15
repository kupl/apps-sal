import sys
input = sys.stdin.readline
from collections import deque, Counter

def bfs():
    q = deque([0])
    dist = [-1]*n
    dist[0] = 0
    
    while q:
        v = q.popleft()
        
        for nv in G[v]:
            if dist[nv]==-1:
                dist[nv] = dist[v]+1
                q.append(nv)
    
    return dist

n = int(input())
p = list(map(int, input().split()))
G = [[] for _ in range(n)]

for i in range(n-1):
    G[i+1].append(p[i]-1)
    G[p[i]-1].append(i+1)

dist = bfs()
cnt = Counter(dist)
ans = 0

for v in cnt.values():
    ans += v%2

print(ans)
