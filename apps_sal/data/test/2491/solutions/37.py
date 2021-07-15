N, M = map(int, input().split())
inf = 10**18
edges = []

for m in range(M):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, -c))

dist = [inf]*N
dist[0] = 0
update = False
for i in range(N):
    for a, b, c in edges:
        if dist[b]>dist[a]+c:
            dist[b] = dist[a]+c
            if b==N-1 and i==N-1:
                update = True

if update:
    print('inf')
else:
    print(-dist[N-1])
