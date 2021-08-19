import sys
input = sys.stdin.readline


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


(N, M, K) = list(map(int, input().split()))
UF = UnionFind(N)
anss = [-1] * N
for _ in range(M):
    (A, B) = list(map(int, input().split()))
    (A, B) = (A - 1, B - 1)
    UF.merge(A, B)
    anss[A] -= 1
    anss[B] -= 1
for i in range(N):
    anss[i] += UF.getSize(i)
for _ in range(K):
    (C, D) = list(map(int, input().split()))
    (C, D) = (C - 1, D - 1)
    if UF.isSame(C, D):
        anss[C] -= 1
        anss[D] -= 1
print(' '.join(map(str, anss)))
