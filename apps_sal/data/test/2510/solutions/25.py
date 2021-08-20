(N, M) = map(int, input().split())


class UnionFind:

    def __init__(self, N):
        self.root = list(range(N + 1))
        self.size = [1] * (N + 1)

    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        (sx, sy) = (self.size[x], self.size[y])
        if sx < sy:
            (x, y) = (y, x)
            (sx, sy) = (sy, sx)
        self.root[y] = x
        self.size[x] += sy

    def find_max(self):
        return max(self.size)


uf = UnionFind(N)
answer = []
append = answer.append
merge = uf.merge
for i in range(M):
    (a, b) = map(int, input().split())
    merge(a, b)
print(uf.find_max())
