from collections import deque


def BFS(graph, a, b):

    q = deque()
    q.append(a)
    visited = [False for _ in range(len(graph))]

    while len(q):
        v = q.pop()

        if visited[v]:
            continue

        for x in graph[v]:
            if not visited[x]:
                q.append(x)

        visited[v] = True

    return visited[b]


n, m = map(int, input().split())
color = {}
for i in range(m):
    v1, v2, c = map(int, input().split())

    if c not in color:
        color[c] = [[] for _ in range(n + 1)]

    color[c][v1].append(v2)
    color[c][v2].append(v1)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())

    ans = 0
    for i in color:
        if BFS(color[i], a, b):
            ans += 1
    print(ans)
