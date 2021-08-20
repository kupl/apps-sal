class Unionfind:

    def __init__(self, n):
        self.par = [x for x in range(n)]
        self.rank = [1] * n
        self.num = [1] * n

    def root(self, a):
        if self.par[a] == a:
            return a
        parent = self.root(self.par[a])
        self.par[a] = parent
        return parent

    def unite(self, a, b):
        (ra, rb) = (self.root(a), self.root(b))
        out = self.num[ra] * self.num[rb]
        if self.rank[ra] < self.rank[rb]:
            (ra, rb) = (rb, ra)
        self.par[rb] = ra
        self.num[ra] += self.num[rb]
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return out

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def com_num(self, a, b):
        if self.same(a, b):
            return 0
        else:
            return self.unite(a, b)


def main():
    (n, m) = map(int, input().split())
    incon = [0] * (m + 1)
    bridge = [0] * m
    uf = Unionfind(n)
    for i in range(m):
        (a, b) = map(int, input().split())
        bridge[i] = (a - 1, b - 1)
    incon[m] = n * (n - 1) // 2
    for i in range(m - 1, -1, -1):
        (a, b) = bridge[i]
        incon[i] = incon[i + 1] - uf.com_num(a, b)
    for i in range(1, m + 1):
        print(incon[i])


main()
