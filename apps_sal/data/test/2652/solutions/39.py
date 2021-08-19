import sys
sys.setrecursionlimit(10 ** 5)


class UnionFind:

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.components = n

    def root(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.root(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        (x, y) = (self.root(x), self.root(y))
        if x != y:
            self.p[x] = y
            self.components -= 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


N = int(input())
(X, Y) = ([], [])
for i in range(N):
    (x, y) = map(int, input().split())
    X.append([x, i])
    Y.append([y, i])
X.sort()
Y.sort()
edges = []
for i in range(N - 1):
    edges.append([X[i + 1][0] - X[i][0], X[i][1], X[i + 1][1]])
    edges.append([Y[i + 1][0] - Y[i][0], Y[i][1], Y[i + 1][1]])
edges.sort()
UF = UnionFind(N)
ans = 0
for (cost, s, t) in edges:
    if UF.same(s, t):
        continue
    UF.unite(s, t)
    ans += cost
print(ans)
