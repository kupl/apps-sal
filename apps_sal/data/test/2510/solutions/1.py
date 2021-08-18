import sys


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


sys.setrecursionlimit(10**9)
input = sys.stdin.readline


sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
u = UnionFind(n)
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    u.unite(a, b)
ans = 0
for i in range(n):
    ans = max(ans, u.size(i))
print(ans)
