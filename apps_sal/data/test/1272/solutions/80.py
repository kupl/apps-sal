class UnionFindWithSize(object):
    """UnionFindTree based on union by size + path compression.
    """

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        (x, y) = (self.find(x), self.find(y))
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.size[y] += self.size[x]
            self.parent[x] = y
        else:
            self.size[x] += self.size[y]
            self.parent[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def sizeofset(self, x):
        return self.size[self.find(x)]


def __starting_point():
    (N, M) = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(lambda x: int(x) - 1, input().split())))
    uf = UnionFindWithSize(N)
    anss = []
    cnt = N * (N - 1) // 2
    for i in range(M - 1, -1, -1):
        anss.append(cnt)
        (a, b) = edges[i]
        if not uf.same(a, b):
            cnt -= uf.sizeofset(a) * uf.sizeofset(b)
            uf.unite(a, b)
    for x in reversed(anss):
        print(x)


__starting_point()
