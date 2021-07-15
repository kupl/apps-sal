

from collections import deque


N,M = list(map(int, input().split()))



es = [[] for _ in range(3*N)]
for _ in range(M):
    u,v = list(map(int, input().split()))
    u,v = u-1, v-1
    es[u].append(N + v)
    es[N + u].append(2*N + v)
    es[2*N + u].append(v)

S,T = list(map(int, input().split()))

q = deque()
q.append(S-1)
INF = float("inf")
dist = [INF] * (3*N)
dist[S-1] = 0

while q:
    curr = q.popleft()
    
    for nxt in es[curr]:
        if dist[nxt] == INF:
            dist[nxt] = dist[curr] + 1
            if nxt == T-1:
                print((dist[nxt] // 3))
                
                return
            
            q.append(nxt)

print((-1))

