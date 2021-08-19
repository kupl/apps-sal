class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


def renketu(n, k, l, pqli, rsli):
    from collections import defaultdict
    ans = []
    pquf = UnionFind(n)
    rsuf = UnionFind(n)
    [pquf.unite(p - 1, q - 1) for (q, p) in pqli]
    [rsuf.unite(r - 1, s - 1) for (r, s) in rsli]
    ansdict = defaultdict(int)
    for i in range(n):
        ansdict[pquf.find(i), rsuf.find(i)] += 1
    for i in range(n):
        ans.append(ansdict[pquf.find(i), rsuf.find(i)])
    return ans


def main():
    (n, k, l) = map(int, input().split())
    pqli = [list(map(int, input().split())) for i in range(k)]
    rsli = [list(map(int, input().split())) for i in range(l)]
    ans = renketu(n, k, l, pqli, rsli)
    print(*ans)


def __starting_point():
    main()


__starting_point()
