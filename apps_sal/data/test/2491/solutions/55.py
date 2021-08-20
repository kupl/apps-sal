def bellman_ford(edges, N, start, end):
    cost = [float('inf') for _ in range(N)]
    cost[start] = 0
    negative = [False for _ in range(N)]
    for i in range(N):
        for j in range(len(edges)):
            (fro, to, c) = edges[j]
            if cost[to] > cost[fro] + c:
                cost[to] = cost[fro] + c
                if i == N - 1:
                    negative[to] = True
    if negative[end]:
        return 'inf'
    else:
        return -cost[end]


(N, M) = list(map(int, input().split()))
edges = []
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    edges.append((a - 1, b - 1, -c))
cost = [float('inf') for _ in range(N)]
start = 0
end = N - 1
print(bellman_ford(edges, N, start, end))
