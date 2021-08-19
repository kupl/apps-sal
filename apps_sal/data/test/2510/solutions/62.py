class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x) -> int:
        return -self.parents[self.find(x)]

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x) -> list:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list:
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self) -> dict:
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))

    def read(self, m):
        for i in range(m):
            (a, b) = list(map(int, input().split()))
            self.union(a - 1, b - 1)

    def solve(self):
        print(max([self.size(i) for i in self.roots()]))


(n, m) = list(map(int, input().split()))
a = UnionFind(n)
a.read(m)
a.solve()
