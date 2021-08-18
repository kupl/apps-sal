import sys
readline = sys.stdin.readline


class UnionFind:
    N = 0
    parent = None
    size = None

    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(self.N)]
        self.size = [1] * self.N

    def root(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]

    def get_group_size(self, x):
        return self.size[self.root(x)]

    def get_roots(self):
        r = set()
        for i in range(self.N):
            r.add(self.root(i))
        return r

    def show_parent(self):
        print(self.parent)

    def show_size(self):
        print(self.size)


N, M = map(int, readline().split())
bridges = [tuple(map(int, readline().split())) for i in range(M)]

UF = UnionFind(N)
ans = [0] * M
num = (N * (N - 1)) // 2

for i in range(len(bridges) - 1, -1, -1):
    ans[i] = num
    a, b = bridges[i]
    a, b = a - 1, b - 1
    if not UF.same(a, b):
        num -= UF.get_group_size(a) * UF.get_group_size(b)
    UF.unite(a, b)

print(*ans, sep="\n")
