import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n - 1)]
    graph = [[] for i in range(n + 1)]
    deg = [0] * (n + 1)
    for (a, b) in ab:
        graph[a].append(b)
        graph[b].append(a)
        deg[a] += 1
        deg[b] += 1
    pnt = [max(deg[i] - 1, 1) for i in range(n + 1)]
    root = 1
    stack = [root]
    dist = [0] * (n + 1)
    dist[root] = pnt[root]
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist[y] == 0:
                dist[y] = dist[x] + pnt[y]
                stack.append(y)
    far = dist.index(max(dist))
    root = far
    stack = [root]
    dist = [0] * (n + 1)
    dist[root] = pnt[root]
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist[y] == 0:
                dist[y] = dist[x] + pnt[y]
                stack.append(y)
    print(max(dist))
