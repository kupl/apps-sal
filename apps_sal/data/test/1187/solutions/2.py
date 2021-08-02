def DFS(graph, status, v):
    status[v] = 1
    for u in graph[v]:
        if status[u] == 1:
            return True
        if status[u] == 0:
            if DFS(graph, status, u):
                return True
    status[v] = 2


def containsCycle(graph):
    n = len(graph)
    status = [0] * n
    for v in range(n):
        if status[v] != 0:
            continue
        if DFS(graph, status, v):
            return True
    return False


nm = input().split()
n = int(nm[0])
m = int(nm[1])

graph = [set() for _ in range(n)]
edges = []
for _ in range(m):
    edge = input().split()
    u = int(edge[0]) - 1
    v = int(edge[1]) - 1
    edges.append((u, v))

    graph[u].add(v)

if (not containsCycle(graph)):
    print(1)
    answer = [1] * m
    print(*answer)
else:
    print(2)
    answer = []
    for e in edges:
        if e[0] > e[1]:
            answer.append(1)
        else:
            answer.append(2)
    print(*answer)
