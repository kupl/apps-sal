from collections import Counter
import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, numV):
        self.pars = list(range(numV))
        self.ranks = [0] * numV

    def find(self, x):
        if self.pars[x] == x:
            return x
        else:
            self.pars[x] = self.find(self.pars[x])
            return self.pars[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.ranks[x] < self.ranks[y]:
            self.pars[x] = y
        else:
            self.pars[y] = x
            if self.ranks[x] == self.ranks[y]:
                self.ranks[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
xys = [tuple(map(int, input().split())) for _ in range(N)]

M = 10**5
UF = UnionFind(2 * M)
for x, y in xys:
    x, y = x - 1, y - 1
    UF.union(x, y + M)

for x in range(2 * M):
    UF.find(x)

cntX = Counter(UF.pars[:M])
cntY = Counter(UF.pars[M:])

ans = 0
for v in list(cntX.keys()):
    ans += cntX[v] * cntY[v]

print((ans - N))
