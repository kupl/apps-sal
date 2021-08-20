class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
(x, y) = ([], [])
for i in range(N):
    (a, b) = list(map(int, input().split()))
    x.append([a, i])
    y.append([b, i])
x.sort()
y.sort()
e = []
for i in range(N - 1):
    e.append([abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]])
    e.append([abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]])
e.sort()
uft = UnionFind(N)
ans = 0
for (w, s, t) in e:
    if not uft.same(s, t):
        uft.union(s, t)
        ans += w
print(ans)
