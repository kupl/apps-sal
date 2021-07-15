import heapq as hq
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))
Q, K = map(int,input().split())
INF = float("inf")
d = [INF]*N
K -= 1
d[K] = 0
q = [(0,K)]
while q:
    dist, i = hq.heappop(q)
    if d[i] < dist:
        continue
    for j, w in edges[i]:
        if d[j] > d[i]+w:
            d[j] = d[i]+w
            hq.heappush(q, (d[j], j))
for _ in range(Q):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    print(d[x]+d[y])
