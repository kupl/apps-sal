class UnionFind:

    def __init__(self, n: int) -> None:
        self.forest = [-1] * n

    def union(self, x: int, y: int) -> None:
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        if self.forest[x] > self.forest[y]:
            (x, y) = (y, x)
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


(n, m, k) = map(int, input().split())
l = [[] for _ in range(n)]
u = UnionFind(n)
for _ in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    u.union(a, b)
    l[a].append(b)
    l[b].append(a)
for _ in range(k):
    (c, d) = map(int, input().split())
    c -= 1
    d -= 1
    if u.issame(c, d):
        l[c].append(d)
        l[d].append(c)
for i in range(n):
    q = u.size(i)
    w = len(l[i])
    print(q - w - 1, end=' ')
