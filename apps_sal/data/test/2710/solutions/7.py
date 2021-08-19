import math


def dfs(u, t, bottleneck, graph, visited):
    if u == t:
        return bottleneck
    visited[u] = True
    for e in graph[u]:
        residual = e.cap - e.flow
        if residual > 0 and not visited[e.v]:
            augment = dfs(e.v, t, min(bottleneck, residual), graph, visited)
            if augment > 0:
                e.flow += augment
                e.reverse.flow -= augment
                return augment
    return 0


def max_flow(G, s, t):
    flow = 0
    augment = 1  # for while to pass
    while augment > 0:
        visited = [False] * len(G)
        augment = dfs(s, t, math.inf, G, visited)
        flow += augment
    return flow


class Edge:
    def __init__(self, v, cap, reverse=None):
        self.cap = cap
        self.v = v
        self.reverse = reverse
        self.flow = 0

    def __repr__(self):
        return str(self.v) + ' (' + str(self.flow) + ')'


n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

sum_a = sum(a)
sum_b = sum(b)

graph = [[] for _ in range(2 * n + 2)]

for i, c in enumerate(a, 1):
    graph[0].append(Edge(i, c))

t = len(graph) - 1
for i, c in enumerate(b, 1 + n):
    graph[i].append(Edge(t, c))

max_cap = math.inf
for i in range(1, len(a) + 1):
    graph[i].append(Edge(i + n, max_cap))  # self edges

for _ in range(m):
    u, v = list(map(int, input().strip().split()))
    graph[u].append(Edge(v + n, max_cap))
    graph[v].append(Edge(u + n, max_cap))


for u, edges in enumerate(graph):
    for edge in edges:
        if edge.reverse is None:
            new_edge = Edge(u, 0, edge)
            edge.reverse = new_edge
            graph[edge.v].append(new_edge)

if sum_a == sum_b and sum_a == max_flow(graph, 0, len(graph) - 1):
    print('YES')
    for i in range(1, n + 1):
        flows = [0] * n
        tot_out = 0
        for edge in graph[i]:
            if edge.v != i + n and edge.flow > 0:
                flows[edge.v - n - 1] = edge.flow
                tot_out += edge.flow
        flows[i - 1] = a[i - 1] - tot_out
        print(' '.join(map(str, flows)))
else:
    print('NO')
