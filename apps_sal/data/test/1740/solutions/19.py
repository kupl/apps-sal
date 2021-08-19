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
        curnode = node
        parent = self.parent

        while parent[curnode] != curnode:
            curnode = parent[curnode]

        root = curnode
        curnode = node

        while parent[curnode] != root:
            parent[curnode] = root

        return root

    def union(self, node, other):
        node = self.find(node)
        other = self.find(other)
        if self.rank[node] > self.rank[other]:
            self.parent[other] = node
            self.ls[node].extend(self.ls[other])

        elif self.rank[other] > self.rank[node]:
            self.parent[node] = other
            self.ls[other].extend(self.ls[node])

        else:
            self.parent[other] = node
            self.ls[node] += self.ls[other]
            self.rank[node] += 1


n = int(input())

ds = DisjointSets(n)
for i in range(n - 1):
    a, b = map(int, input().split())
    ds.union(a, b)
# print(ds.rank)
# print(ds.parent)
ans = ds.ls[ds.find(1)]
for a in ans:
    print(a, end=" ")
