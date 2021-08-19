class UnionFindWithSize:

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
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        uf = UnionFindWithSize(N)
        for j in range(M):
            if j != i:
                (a, b) = edges[j]
                uf.unite(a, b)
        if uf.sizeofset(0) != N:
            ans += 1
    print(ans)


__starting_point()
