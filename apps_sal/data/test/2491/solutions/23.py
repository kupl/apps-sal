N, M = map(int, input().split())
edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, -c])
def bellman_ford(edges, N):
    dist = [float('inf') for i in range(N)]
    dist[0] = 0
    for i in range(N-1):
        for edge in edges:
            if dist[edge[1] - 1] > dist[edge[0] - 1] + edge[2]:
                dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]
    negative = [False] * N

    for i in range(N):
        for edge in edges:
            if dist[edge[1] - 1] > dist[edge[0] - 1] + edge[2]:
                dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]
                negative[edge[1] - 1] = True
            if negative[edge[0] - 1] == True:
                negative[edge[1] - 1] =True
    
    return 'inf' if negative[-1] else -dist[-1]

print(bellman_ford(edges, N))
