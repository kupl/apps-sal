from sys import stdin
__author__ = 'artyom'


def read_int_ary():
    return map(int, stdin.readline().strip().split())


def dfs(graph, start):
    (visited, tree, processed, stack) = (set(), [], set(), [start])
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        if not vertex in processed:
            tree.append(vertex)
        processed.add(vertex)
    return tree


(n, m, k) = read_int_ary()
grid = []
for i in range(n):
    grid.append(list(stdin.readline().strip()))
graph = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            v = (i, j)
            graph[v] = set()
            if i > 0 and grid[i - 1][j] == '.':
                u = (i - 1, j)
                graph[v].add(u)
                graph[u].add(v)
            if j > 0 and grid[i][j - 1] == '.':
                u = (i, j - 1)
                graph[v].add(u)
                graph[u].add(v)
processed = dfs(graph, next(iter(graph.keys())))
added = set()
while len(added) < k:
    vertex = processed.pop()
    grid[vertex[0]][vertex[1]] = 'X'
    added.add(vertex)
for i in range(n):
    print(''.join(grid[i]))
