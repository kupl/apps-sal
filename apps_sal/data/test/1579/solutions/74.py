from operator import itemgetter
from collections import defaultdict
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
xys = []
for i in range(N):
    x, y = list(map(int, input().split()))
    xys.append((x, y, i))

UF = UnionFind(N)
for k in range(2):
    xys.sort(key=itemgetter(k))
    for i in range(N - 1):
        if xys[i][k] == xys[i + 1][k]:
            UF.union(xys[i][2], xys[i + 1][2])

Xs = defaultdict(set)
Ys = defaultdict(set)
for x, y, i in xys:
    no = UF.find(i)
    Xs[no].add(x)
    Ys[no].add(y)

ans = 0
for no in list(Xs.keys()):
    ans += len(Xs[no]) * len(Ys[no])

print((ans - N))
