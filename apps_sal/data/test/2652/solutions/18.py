import sys
from collections import defaultdict
def finput(): return sys.stdin.readline().strip()


class Unionfind():
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.ranks[x] < self.ranks[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        if self.ranks[x] == self.ranks[y]:
            self.ranks[x] += 1

    def size(self, x):
        return -self.parents[self.find(x)]

    def issametree(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n = int(finput())
    coor = [list(map(int, finput().split())) + [i] for i in range(n)]
    coor.sort(key=lambda e: e[0])
    def cost(e, f): return min(abs(e[0] - f[0]), abs(e[1] - f[1]))
    ew = dict(((coor[i][2], coor[i + 1][2]), cost(coor[i][:2], coor[i + 1][:2])) for i in range(n - 1))
    coor.sort(key=lambda e: e[1])
    ew.update(dict(((coor[i][2], coor[i + 1][2]), cost(coor[i][:2], coor[i + 1][:2])) for i in range(n - 1)))
    edges = sorted(list(iter(ew)), key=lambda e: ew[e])
    v = Unionfind(n)
    totcost = 0
    for edge in edges:
        if not v.issametree(edge[0], edge[1]):
            v.union(edge[0], edge[1])
            totcost += ew[edge]
    print(totcost)


def __starting_point():
    main()


__starting_point()
