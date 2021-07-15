class UnionFind:
    def __init__(self, N):
        self.root = [-1 for _ in range(N)]
        self.size = [1 for _ in range(N)]

    def find(self, x):
        while self.root[x] >= 0:
            x = self.root[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.root[x] = y
            self.size[y] += self.size[x]
        else:
            self.root[y] = x
            self.size[x] += self.size[y]

N, M = [int(_) for _ in input().split()]
uf = UnionFind(N)

for i in range(M):
    X, Y, Z = [int(_) for _ in input().split()]
    uf.union(X-1, Y-1)

ans = set()
for i in range(N):
    ans.add(uf.find(i))
print((len(ans)))

