N = int(input())
edges = []
for i in range(N - 1):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])


def BFS(K, edges, N):
    roots = [[] for i in range(N)]
    for a, b, c in edges:
        roots[a - 1] += [(b - 1, c)]
        roots[b - 1] += [(a - 1, c)]
    dist = [-1] * N
    stack = []
    stack.append(K)
    dist[K] = 0
    while stack:
        label = stack.pop(-1)
        for i, c in roots[label]:
            if dist[i] == -1:
                dist[i] = dist[label] + c
                stack += [i]
    return dist


Q, K = map(int, input().split())
K = K - 1
dist = BFS(K, edges, N)
lsxy = []
for i in range(Q):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    lsxy.append([x, y])
for i in lsxy:
    print(dist[i[0]] + dist[i[1]])
