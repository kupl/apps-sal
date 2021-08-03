mod = 998244353
nn = 1010
fa = [1] * (nn + 1)
fainv = [1] * (nn + 1)
for i in range(nn):
    fa[i + 1] = fa[i] * (i + 1) % mod
fainv[-1] = pow(fa[-1], mod - 2, mod)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i + 1] * (i + 1) % mod

N, K = map(int, input().split())
X = [[int(a) for a in input().split()] for _ in range(N)]


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.PA = [-1] * n

    def root(self, a):
        L = []
        while self.PA[a] >= 0:
            L.append(a)
            a = self.PA[a]
        for l in L:
            self.PA[l] = a
        return a

    def unite(self, a, b):
        ra, rb = self.root(a), self.root(b)
        if ra != rb:
            if self.PA[rb] >= self.PA[ra]:
                self.PA[ra] += self.PA[rb]
                self.PA[rb] = ra
            else:
                self.PA[rb] += self.PA[ra]
                self.PA[ra] = rb

    def size(self, a):
        return - self.PA[self.root(a)]

    def groups(self):
        G = [[] for _ in range(self.n)]
        for i in range(self.n):
            G[self.root(i)].append(i)
        return [g for g in G if g]

    def group_size(self):
        G = [[] for _ in range(self.n)]
        for i in range(self.n):
            G[self.root(i)].append(i)
        return [len(g) for g in G if g]


ans = 1
uf1 = UnionFind(N)
s = 0
for i in range(N):
    for j in range(i):
        for k in range(N):
            if X[i][k] + X[j][k] > K:
                break
        else:
            uf1.unite(i, j)
for a in uf1.group_size():
    ans = ans * fa[a] % mod

uf2 = UnionFind(N)
s = 0
for i in range(N):
    for j in range(i):
        for k in range(N):
            if X[k][i] + X[k][j] > K:
                break
        else:
            uf2.unite(i, j)
for a in uf2.group_size():
    ans = ans * fa[a] % mod

print(ans)
