class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n = int(input())
graphx = []
graphy = []

for i in range(n):
    x, y = map(int, input().split())
    graphx.append((x, y, i))
    graphy.append((x, y, i))
graphx = sorted(graphx, key=lambda x: x[0])
graphy = sorted(graphy, key=lambda x: x[1])
graph = []


for k in range(n - 1):
    i, j = graphx[k][2], graphx[k + 1][2]
    x0, x1 = graphx[k][0], graphx[k + 1][0]
    m = abs(x0 - x1)
    graph.append((m, i, j))

for k in range(n - 1):
    i, j = graphy[k][2], graphy[k + 1][2]
    y0, y1 = graphy[k][1], graphy[k + 1][1]
    m = abs(y0 - y1)
    graph.append((m, i, j))


graph.sort()
# print(graph)

ans = 0
uf = UnionFind(n)
for c, i, j in graph:
    if not uf.same(i, j):
        ans += c
        uf.union(i, j)
print(ans)
