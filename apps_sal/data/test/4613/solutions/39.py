class UnionFind:
    def __init__(self, N):
        self.N = N

        self.parent = [-1] * N

    def root(self, i):
        if self.parent[i] < 0:
            return i

        r = self.root(self.parent[i])
        self.parent[i] = r
        return r

    def unite(self, i, j):
        i = self.root(i)
        j = self.root(j)

        if i == j:
            return

        if i > j:
            i, j = j, i

        self.parent[i] += self.parent[j]
        self.parent[j] = i

    def same(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, i):
        return -self.parent[self.root(i)]

    def roots(self):
        return [self.root(i) for i in range(self.N)]

    def groupcount(self):
        return len(set(self.roots()))


N, M = map(int, input().split())
edges = [[int(x) - 1 for x in input().split()] for _ in range(M)]

ans = 0

for i in range(M):
    forest = UnionFind(N)

    for i, j in edges[:i] + edges[i + 1:]:
        forest.unite(i, j)

    if forest.groupcount() != 1:
        ans += 1

print(ans)
