from collections import Counter
import sys
read = sys.stdin.readline


def MAP():
    return map(int, read().split())


def I():
    return int(read())


def LI():
    return list(map(int, read().split()))


MOD = 998244353


class UnionFind:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.siz = [1 for _ in range(N)]
        self.rank = [0 for _ in range(N)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return 0
        else:
            if self.rank[a] > self.rank[b]:
                self.par[b] = a
                self.siz[a] += self.siz[b]
            else:
                self.par[a] = b
                self.siz[b] += self.siz[a]
                if self.rank[a] == self.rank[b]:
                    self.rank[b] += 1

    def size(self, a):
        return self.siz[self.find(a)]

    def same(self, a, b):
        return self.find(a) == self.find(b)


N, K = MAP()
a = [LI() for _ in range(N)]
UFg = UnionFind(N)
UFr = UnionFind(N)
fac = [1] * (N + 1)
for i in range(2, N + 1):
    fac[i] = fac[i - 1] * i % MOD

for i in range(N):
    for j in range(i):
        isokg = True
        isokr = True
        for k in range(N):
            if a[i][k] + a[j][k] > K:
                isokg = False
            if a[k][i] + a[k][j] > K:
                isokr = False
        if isokg:
            UFg.union(i, j)
        if isokr:
            UFr.union(i, j)

dicg = Counter([UFg.find(i) for i in range(N)])
dicr = Counter([UFr.find(i) for i in range(N)])

resg, resr = 1, 1
for x, size in dicg.items():
    resg = resg * fac[size] % MOD
for y, size in dicr.items():
    resr = resr * fac[size] % MOD
print(resg * resr % MOD)
