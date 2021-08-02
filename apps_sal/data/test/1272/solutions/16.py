class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x

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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return abs(self.parents[self.find(x)])


N, M = map(int, input().split())
uf = UnionFind(N + 1)

cnt = (N) * (N - 1) // 2
L = [[int(x) for x in input().split()] for _ in range(M)]
ans = []

for a, b in L[::-1]:
    ans.append(cnt)
    if not uf.same(a, b):
        cnt -= uf.size(a) * uf.size(b)
        uf.union(a, b)

for x in ans[::-1]:
    print(x)
