class PotentialUnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.weight = [0] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            px = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = px
            return px

    def weight(self, x):
        self.find(x)
        return self.weight[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.find(x)

    def unite(self, x, y, w):
        w += self.weight[x] - self.weight[y]
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            (x, y) = (y, x)
            w = -w
        self.par[x] += self.par[y]
        self.par[y] = x
        self.weight[y] = w
        return True

    def diff(self, x, y):
        return self.weight[y] - self.weight[x]


(n, m) = list(map(int, input().split()))
PUF = PotentialUnionFind(n)
flag = 0
for _ in range(m):
    (l, r, d) = list(map(int, input().split()))
    l -= 1
    r -= 1
    if PUF.is_same(l, r):
        if abs(PUF.diff(l, r)) == d:
            continue
        else:
            flag = 1
    else:
        PUF.unite(l, r, d)
print('No' if flag else 'Yes')
