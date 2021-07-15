import heapq
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a - 1].append([c, b - 1])
    G[b - 1].append([c, a - 1])
Q, K = map(int, input().split())

def dijkstra(s, N, G):
    d = [float('inf')] * N
    d[s] = 0
    hq = [[0, s]]
    heapq.heapify(hq)
    while len(hq) > 0:
        v, i = heapq.heappop(hq)
        if d[i] < v:
            continue
        for c, j in G[i]:
            if d[j] > d[i] + c:
                d[j] = d[i] + c
                heapq.heappush(hq, [d[j], j])
    return d

D = dijkstra(K - 1, N, G)

dist = [0] * Q
for i in range(Q):
    x, y = map(int, input().split())
    dist[i] = D[x - 1] + D[y - 1]

for d in dist:
    print(d)
