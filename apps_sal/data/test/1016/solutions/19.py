def recursive_dfs(graph, start, path=[]):
    """recursive depth first search from start"""
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path


def iterative_dfs(graph, start, path=[]):
    """iterative depth first search from start"""
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = graph[v] + q
    return path


def iterative_bfs(graph, start, path=[]):
    """iterative breadth first search from start"""
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            path = path + [v]
            q = q + graph[v]
    return path


(nodes, edges) = list(map(int, input().split(' ')))
graph = {}
for i in range(nodes):
    graph[i] = []
for i in range(edges):
    (a, b) = list(map(int, input().split(' ')))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
marked = [False] * nodes
num = 0
for i in range(nodes):
    if not marked[i]:
        for j in iterative_dfs(graph, i):
            marked[j] = True
        num += 1
print(2 ** (nodes - num))
