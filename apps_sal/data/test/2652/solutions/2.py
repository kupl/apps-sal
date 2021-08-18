class UnionFind:
    def __init__(self, n):
        self.v = [-1] * n

    def find(self, x):
        if self.v[x] < 0:
            return x
        else:
            self.v[x] = self.find(self.v[x])
            return self.v[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.v[x] > self.v[y]:
                x, y = y, x
            self.v[x] += self.v[y]
            self.v[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.v[self.find(x)]


def main():
    from operator import itemgetter
    import sys
    input = sys.stdin.readline

    N = int(input())

    ps = []
    xs = set()
    ys = set()
    for i in range(N):
        x, y = list(map(int, input().split()))
        ps.append((x, y))
        xs.add(x)
        ys.add(y)

    xs = tuple(sorted(xs))
    ys = tuple(sorted(ys))

    dx = {e: i for i, e in enumerate(xs)}
    dy = {e: i for i, e in enumerate(ys)}

    uf = UnionFind(N * 2)
    for x, y in ps:
        uf.unite(dx[x], dy[y] + N)

    def make_edges(xs, start):
        xes = []
        for i, (x0, x1) in enumerate(zip(xs, xs[1:]), start=start):
            xes.append((abs(x1 - x0), i, i + 1))
        return xes

    xes = make_edges(xs, start=0)
    yes = make_edges(ys, start=N)

    ret = 0
    for cost, a, b in sorted(xes + yes, key=itemgetter(0)):
        if uf.same(a, b):
            continue
        uf.unite(a, b)
        ret += cost
    print(ret)


def __starting_point():
    main()


__starting_point()
