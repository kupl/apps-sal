# longest version bellman ford
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))


inf = float("inf")
dist = [-inf for i in range(N)]
dist[0] = 0
is_cycle = False

# 辺の緩和
for i in range(N):
    for edge in edges:
        new_dist = dist[edge[0]] + edge[2]
        if dist[edge[1]] < new_dist:
            dist[edge[1]] = new_dist
            if i == N - 1 and edge[1] == N - 1:
                is_cycle = True

ans = dist[-1] if not is_cycle else 'inf'
print(ans)
