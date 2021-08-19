class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] is x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def __starting_point():
    import sys
    import threading


class graph:

    def __init__(self, n):
        self.size = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, node):
        self.visited[node] = True
        subg = [node]
        for edge in self.adj[node]:
            if not self.visited[edge]:
                subg.extend(self.DFS(edge))
        return subg

    def components(self):
        self.visited = [False] * self.size
        self.components = []
        for node in range(self.size):
            if self.visited[node] is False:
                self.components.append(self.DFS(node))
        return self.components


def __starting_point():
    (n, m, k) = [int(x) for x in input().split()]
    uf = UnionFind(n)
    color = [int(x) for x in input().split()]
    for _ in range(m):
        (u, v) = [int(x) for x in input().split()]
        uf.union(u - 1, v - 1)
    collection = [[] for i in range(n)]
    for i in range(n):
        collection[uf.find(i)].append(i)
    ans = 0
    for sock_set in collection:
        if not sock_set:
            continue
        count = {}
        set_max = 1
        for sock in sock_set:
            try:
                count[color[sock]] += 1
                set_max = max(count[color[sock]], set_max)
            except:
                count[color[sock]] = 1
        ans += len(sock_set) - set_max
    print(ans)


__starting_point()
