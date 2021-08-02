from itertools import combinations


class unionfind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def root(self, a):
        if self.par[a] == a: return a
        parent = self.root(self.par[a])
        self.par[a] = parent
        return parent

    def unite(self, a, b):
        ra, rb = self.root(a), self.root(b)
        if ra == rb: return
        if self.rank[ra] > self.rank[rb]:
            ra, rb = rb, ra
        self.par[rb] = ra
        self.rank[ra] += 1

    def same(self, a, b):
        return self.root(a) == self.root(b)


def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    sm = 0
    for e_remove in edges:
        uf = unionfind(n)
        for e in edges:
            if e == e_remove: continue
            uf.unite(e[0] - 1, e[1] - 1)

        for a in combinations(range(n), 2):
            if not uf.same(a[0], a[1]):
                break
        else: continue
        sm += 1

    print(sm)


main()
