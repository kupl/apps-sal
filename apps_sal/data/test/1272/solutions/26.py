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
        x, y = self.getRoot(x), self.getRoot(y)
        sx, sy = self.sizes[x], self.sizes[y]
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


n, m = map(int, input().split())
e = [list(map(int, input().split())) for i in range(m)]
e.reverse()

uf = UnionFind(n)
score = n * (n - 1) // 2
ans = [score]
for ce in range(m - 1):
    u, v = e[ce][0] - 1, e[ce][1] - 1
    if uf.getRoot(u) != uf.getRoot(v):
        xu = uf.getSize(u)
        xv = uf.getSize(v)
        uf.merge(u, v)
        score -= xu * xv
    ans.append(score)
ans.reverse()

for i in range(m):
    print(ans[i])
