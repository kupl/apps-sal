class DisjointSet:
    def __init__(self, size):
        self.rank = [0 for i in range(size)]
        self.p = [0 for i in range(size)]
        for i in range(size):
            self.makeSet(i)

    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]


def __starting_point():
    maxxy = 10**5
    N = int(input())
    ds = DisjointSet(maxxy * 2 + 1)
    left = [0 for i in range(maxxy * 2 + 1)]
    right = [0 for i in range(maxxy * 2 + 1)]
    for i in range(N):
        x, y = list(map(int, input().split()))
        ds.unite(x, maxxy + y)
    for i in range(maxxy + 1):
        left[ds.findSet(i)] += 1
    for i in range(maxxy + 1, maxxy * 2 + 1):
        right[ds.findSet(i)] += 1
    ans = 0
    for i in range(maxxy * 2 + 1):
        ans += left[i] * right[i]
    ans -= N
    print(ans)


__starting_point()
