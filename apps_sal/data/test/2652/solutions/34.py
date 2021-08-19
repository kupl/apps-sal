n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
(x, y) = zip(*xy)
x = list(zip(range(n), x))
y = list(zip(range(n), y))
x.sort(key=lambda a: a[1])
y.sort(key=lambda a: a[1])
d = []
for i in range(n - 1):
    d.append([x[i + 1][1] - x[i][1], x[i + 1][0], x[i][0]])
    d.append([y[i + 1][1] - y[i][1], y[i + 1][0], y[i][0]])
d.sort(key=lambda a: a[0], reverse=True)


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


ans = 0
uf = UnionFind(n)
while d:
    (dist, i, j) = d.pop()
    if uf.same(i, j):
        continue
    uf.union(i, j)
    ans += dist
print(ans)
