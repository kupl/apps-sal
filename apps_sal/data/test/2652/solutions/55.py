
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def resolve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append((i, x))
        Y.append((i, y))

    X.sort(key=lambda x: x[1])
    Y.sort(key=lambda x: x[1])

    G = []
    for i in range(1, N):
        a, x1 = X[i - 1]
        b, x2 = X[i]
        G.append((a, b, x2 - x1))
        a, y1 = Y[i - 1]
        b, y2 = Y[i]
        G.append((a, b, y2 - y1))

    ans = 0
    uf = UnionFind(N)
    G.sort(key=lambda x: x[2])
    for a, b, w in G:
        if not uf.is_same(a, b):
            uf.union(a, b)
            ans += w
    print(ans)


def __starting_point():
    resolve()


__starting_point()
