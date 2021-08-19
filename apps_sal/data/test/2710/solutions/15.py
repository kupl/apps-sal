import math


class Edge:
    def __init__(self, c, f, t, rev=None):
        self.capacity = c
        self.flow = f
        self.target = t
        # Reversed edges have capacity of 0
        self.rev = rev

    def __repr__(self):
        return "<e: (cap: {}, target: {}, flow: {}>".format(self.capacity, self.target, self.flow)


def search(u, t, smallest, visited, graph):
    if u == t:
        return smallest
    visited[u] = True
    for e in graph[u]:
        residual = e.capacity - e.flow
        if residual > 0 and not visited[e.target]:
            augment = search(e.target, t, min(smallest, residual), visited, graph)
            if augment > 0:
                e.flow += augment
                e.rev.flow -= augment
                return augment
    return 0


def fulkerson(g, s, t):
    flow = 0
    while True:
        Visited = [False for _ in range(len(g))]
        augment = search(s, t, math.inf, Visited, g)
        flow += augment
        if augment <= 0:
            break
    return flow


def print_graph(graph):
    for i, edges in enumerate(graph):
        print("{}: [{}]".format(i, edges))


def main():
    [n, m] = list(map(int, input("").split()))

    have = list(map(int, input("").split()))
    need = list(map(int, input("").split()))

    # index 0 is start. Index 2n+1 is sink node.
    graph = [[] for _ in range(2 * n + 2)]

    # Source to initial cities.
    for i, soldiers in enumerate(have):
        graph[0].append(Edge(soldiers, 0, i + 1))

    # Set up edges to sink.
    for i, soldiers in enumerate(need):
        graph[n + i + 1].append(Edge(soldiers, 0, 2 * n + 1))

    # Set up paths
    for _ in range(m):
        [s, t] = list(map(int, input("").split()))
        graph[t].append(Edge(1000, 0, n + s))
        graph[s].append(Edge(1000, 0, n + t))

    # Set up staying soldiers.
    for i in range(n):
        i = i + 1
        graph[i].append(Edge(have[i - 1], 0, n + i))

    # Create residual graph
    residualGraph = [[] for _ in range(len(graph))]
    # Generate residuals
    for u, edges in enumerate(graph):
        for e in edges:
            target = e.target
            # Circular link
            reverse = Edge(0, 0, u, e)
            e.rev = reverse

            residualGraph[u].append(e)
            residualGraph[target].append(reverse)

    flow = fulkerson(residualGraph, 0, 2 * n + 1)
    if sum(need) != flow or sum(have) != sum(need):
        print("NO")
    else:
        print("YES")
        adjmatrix = [[0 for _ in range(n)] for _ in range(n)]

        for u, edges in enumerate(residualGraph[1:2 * n + 1]):
            u = u + 1
            for e in edges:
                if e.capacity == 1000 or (u + n == e.target and e.target != 2 * n + 1):
                    adjmatrix[u - 1][e.target - n - 1] = e.flow

        for row in adjmatrix:
            print(" ".join(map(str, row)))

# run this bad boy


def __starting_point():
    main()


__starting_point()
