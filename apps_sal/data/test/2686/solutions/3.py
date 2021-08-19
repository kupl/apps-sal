from collections import deque


def bfs(graph, u, t):
    queue = deque([u])
    level = {u: 0}
    while queue:
        ver = queue.popleft()
        for v in graph[ver]:
            if v not in level:
                queue.append(v)
                level[v] = level[ver] + 1
    return level.get(t, 0)


try:
    (n, e) = map(int, input().split())
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for _ in range(e):
        (a, b) = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    (s, t) = map(int, input().split())
    p = bfs(graph, s, t)
    print(p)
except:
    pass
