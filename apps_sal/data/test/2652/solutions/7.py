import sys
import collections
sys.setrecursionlimit(10 ** 8)


def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]


class UnionFind:
    def __init__(self, size):
        self.par = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return

    def same(self, x, y): return self.find(x) == self.find(y)


def main():
    N = Z()
    Cs = [ZZ() + [i] for i in range(N)]
    X = sorted(Cs)
    Y = sorted(Cs, key=lambda x: x[1])
    es = []
    for i in range(N - 1):
        c = X[i + 1][0] - X[i][0]
        u, v = X[i][2], X[i + 1][2]
        es.append([c, u, v])
    for i in range(N - 1):
        c = Y[i + 1][1] - Y[i][1]
        u, v = Y[i][2], Y[i + 1][2]
        es.append([c, u, v])
    es.sort()
    uf = UnionFind(N)
    output = 0
    for i in range(len(es)):
        c, u, v = es[i]
        if not uf.same(u, v):
            uf.unite(u, v)
            output += c
    print(output)

    return


def __starting_point():
    main()


__starting_point()
