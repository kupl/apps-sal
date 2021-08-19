[N, M] = list(map(int, input().split()))
edges = [[] for _ in range(N + 1)]
edge_in = []
for _ in range(M):
    [u, v] = list(map(int, input().split()))
    edge_in.append([u, v])
    edges[u].append(v)
seen = [False for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


def bfs(node):
    visited[node] = True
    seen[node] = True
    for v in edges[node]:
        if not seen[v] and visited[v]:
            continue
        if seen[v] or bfs(v):
            return True
    seen[node] = False
    return False


hasCycle = False
for i in range(1, N + 1):
    if visited[i]:
        continue
    if bfs(i):
        hasCycle = True
        break
if not hasCycle:
    print(1)
    print(' '.join(['1' for _ in range(M)]))
else:
    print(2)
    print(' '.join(['1' if u < v else '2' for (u, v) in edge_in]))
