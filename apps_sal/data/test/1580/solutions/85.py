import sys
sys.setrecursionlimit(10 ** 9)
(N, M) = list(map(int, input().split()))


class Union_Find:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        elif self.rank[px] == self.rank[py]:
            self.parent[py] = px
            self.rank[px] += 1
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py


uftree = Union_Find(N + 1)
for i in range(M):
    (x, y, _) = list(map(int, input().split()))
    uftree.unite(x, y)
result = 0
for i in range(1, N + 1):
    if uftree.find(i) == i:
        result += 1
print(result)
