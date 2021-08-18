from collections import deque
infty = 10 ** 9


def BFS(graph, parent, u):
    queue = deque()
    queue.append(u)
    visited = [False for k in range(len(parent))]
    visited[u] = True
    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                parent[j] = v


n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
parent = [-1 for i in range(n)]
BFS(graph, parent, 0)
if -1 in parent[1:]:
    print("No")
else:
    print("Yes")
    for p in parent[1:]:
        print(p + 1)
