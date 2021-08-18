class DisjointSets:
    parent = {}
    rank = {}
    ls = {}

    def __init__(self, n):
        for i in range(1, n + 1):
            self.makeSet(i)

    def makeSet(self, node):
        self.node = node
        self.parent[node] = node
        self.rank[node] = 1
        self.ls[node] = [node]

    def find(self, node):
        parent = self.parent
        if parent[node] != node:
            parent[node] = self.find(parent[node])
        return parent[node]

    def union(self, node, other):
        node = self.find(node)
        other = self.find(other)
        rank = self.rank
        parent = self.parent
        ls = self.ls

        if rank[node] > rank[other]:
            parent[other] = node
            ls[node].extend(ls[other])

        elif rank[other] > rank[node]:
            parent[node] = other
            ls[other].extend(ls[node])

        else:
            parent[other] = node
            ls[node] += ls[other]
            rank[node] += 1


n = int(input())

ds = DisjointSets(n)
for i in range(n - 1):
    a, b = map(int, input().split())
    ds.union(a, b)
ans = ds.ls[ds.find(1)]
for a in ans:
    print(a, end=" ")
