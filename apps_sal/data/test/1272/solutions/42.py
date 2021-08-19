class UnionFind:
    def __init__(self, N):
        self.N = N

        # the parent of all node is itself
        # self.parent = list(range(N))
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
        # print(self.parent)

    def same(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, i):
        return -self.parent[self.root(i)]

    def roots(self):
        return [self.root(i) for i in range(self.N)]

    def groupcount(self):
        return len(set(self.roots()))


N, M = map(int, input().split())

# init union find
forest = UnionFind(N)

edges = []
for _ in range(M):
    edges.append([int(e) - 1 for e in input().split()])

inconvenience = N * (N - 1) // 2
score = []
for a, b in edges[::-1]:
    score.append(inconvenience)

    if not forest.same(a, b):
        inconvenience -= forest.size(a) * forest.size(b)

    forest.unite(a, b)

for s in score[::-1]:
    print(s)
