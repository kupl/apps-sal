class UnionFind:
    def __init__(self, n: int) -> None:
        self.forest = [-1] * n

    def union(self, x: int, y: int) -> None:
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        if self.forest[x] > self.forest[y]:
            x, y = y, x
        self.forest[x] += self.forest[y]
        self.forest[y] = x
        return

    def findRoot(self, x: int) -> int:
        if self.forest[x] < 0:
            return x
        else:
            self.forest[x] = self.findRoot(self.forest[x])
            return self.forest[x]

    def issame(self, x: int, y: int) -> bool:
        return self.findRoot(x) == self.findRoot(y)

    def size(self, x: int) -> int:
        return -self.forest[self.findRoot(x)]


n, m, k = list(map(int, input().split()))
u = UnionFind(n)
dire = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    dire[a - 1].append(b - 1)
    dire[b - 1].append(a - 1)
    u.union(a - 1, b - 1)
for i in range(k):
    c, d = list(map(int, input().split()))
    if u.issame(c-1,d-1):
        dire[c - 1].append(d - 1)
        dire[d - 1].append(c - 1)

print((*[u.size(i) - len(dire[i]) - 1 for i in range(n)]))

