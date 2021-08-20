class Union_Find:

    def __init__(self, num):
        self.par = [-1] * (num + 1)
        self.siz = [1] * (num + 1)

    def same_checker(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.siz[ry] += self.siz[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
        return

    def size(self, x):
        return self.siz[self.find(x)]


n = int(input())
uf = Union_Find(n)
d = [list(map(int, input().split())) for i in range(n)]
x = [[] for i in range(100001)]
y = [[] for i in range(100001)]
for i in range(n):
    (xi, yi) = d[i]
    x[xi].append(i + 1)
    y[yi].append(i + 1)
for i in range(1, 100001):
    for j in range(len(x[i]) - 1):
        uf.union(x[i][j], x[i][j + 1])
for i in range(1, 100001):
    for j in range(len(y[i]) - 1):
        uf.union(y[i][j], y[i][j + 1])
par = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    par[uf.find(i)].append(d[i - 1])
ans = -n
for i in range(1, n + 1):
    x = set()
    y = set()
    for (xi, yi) in par[i]:
        x.add(xi)
        y.add(yi)
    ans += len(x) * len(y)
print(ans)
