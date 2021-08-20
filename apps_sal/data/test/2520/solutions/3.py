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
            (i, j) = (j, i)
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


(N, M, K) = map(int, input().split())
notfriend = [set() for _ in range(N)]
forest = UnionFind(N)
for i in range(M):
    (a, b) = map(int, input().split())
    (a, b) = (a - 1, b - 1)
    notfriend[a].add(b)
    notfriend[b].add(a)
    forest.unite(a, b)
for i in range(K):
    (a, b) = map(int, input().split())
    (a, b) = (a - 1, b - 1)
    if forest.same(a, b):
        notfriend[a].add(b)
        notfriend[b].add(a)
ans = ' '.join([str(forest.size(i) - 1 - len(notfriend[i])) for i in range(N)])
print(ans)
