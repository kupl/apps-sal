from collections import defaultdict


class Graph(object):
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def __getitem__(self, index):
        return self._graph[index]


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


n, m = list(map(int, input().split()))
g = list(map(int, input().split()))
f = [list(map(int, input().split()))for _ in range(m)]
v = Graph(f)
fg = []
vi = [False] * n
for i in range(0, n):
    if vi[i]:
        continue
    cc = bfs(v, i + 1)
    for e in cc:
        vi[e - 1] = True
    fg.append(cc)
print(sum(min(g[e - 1] for e in _g) for _g in fg))
