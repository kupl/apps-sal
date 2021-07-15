from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    G[l].append([r, d])
    G[r].append([l, -d])
INF = float('inf')
dist = [INF]*N
seen = [False]*N
q = deque([])
for s in range(N):
    if dist[s] != INF:
        continue
    q.append([s,0])
    while len(q) != 0:
        p = q.popleft()
        if seen[p[0]] and dist[p[0]] != p[1]:
            print('No')
            return
        elif seen[p[0]] and dist[p[0]] == p[1]:
            continue
        else:
            dist[p[0]] = p[1]
            seen[p[0]] = True
            for np in G[p[0]]:
                q.append([np[0], p[1] + np[1]])
print('Yes')
