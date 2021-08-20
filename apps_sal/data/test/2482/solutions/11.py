from collections import defaultdict


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            (x, y) = (y, x)
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    (n, k, l) = map(int, input().split())
    road = UnionFind(n)
    train = UnionFind(n)
    for _ in range(k):
        (p, q) = map(int, input().split())
        road.unite(p - 1, q - 1)
    for _ in range(l):
        (r, s) = map(int, input().split())
        train.unite(r - 1, s - 1)
    d = defaultdict(int)
    for i in range(n):
        d[road.find(i), train.find(i)] += 1
    ans = []
    for i in range(n):
        ans.append(d[road.find(i), train.find(i)])
    print(*ans)


def __starting_point():
    main()


__starting_point()
