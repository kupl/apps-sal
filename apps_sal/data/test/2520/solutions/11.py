class UnionFind:

    def __init__(self, numV):
        self.pars = list(range(numV))
        self.ranks = [0] * numV
        self.sizes = [1] * numV

    def getRoot(self, x):
        par = self.pars[x]
        if par != x:
            self.pars[x] = par = self.getRoot(par)
        return par

    def merge(self, x, y):
        (x, y) = (self.getRoot(x), self.getRoot(y))
        (sx, sy) = (self.sizes[x], self.sizes[y])
        if x == y:
            return (0, 0)
        if self.ranks[x] < self.ranks[y]:
            self.pars[x] = y
            self.sizes[y] += sx
        else:
            self.pars[y] = x
            self.sizes[x] += sy
            if self.ranks[x] == self.ranks[y]:
                self.ranks[x] += 1
        return (sx, sy)

    def isSame(self, x, y):
        return self.getRoot(x) == self.getRoot(y)

    def updatePars(self):
        for v in range(len(self.pars)):
            self.getRoot(v)

    def getSize(self, x):
        return self.sizes[self.getRoot(x)]


(n, m, k) = map(int, input().split())
uf = UnionFind(n)
ex = [[] for i in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    uf.merge(a, b)
    ex[a].append(b)
    ex[b].append(a)
for i in range(k):
    (c, d) = map(int, input().split())
    c -= 1
    d -= 1
    if uf.getRoot(c) == uf.getRoot(d):
        ex[c].append(d)
        ex[d].append(c)
ans = []
for i in range(n):
    r = uf.getRoot(i)
    ans.append(uf.sizes[r] - len(list(set(ex[i]))) - 1)
ans = [str(i) for i in ans]
print(' '.join(ans))
