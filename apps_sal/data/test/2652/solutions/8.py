import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


class UnionFind:
    # Reference: https://note.nkmk.me/python-union-find/
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

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, *XY = list(map(int, read().split()))
    X = list(zip(XY[::2], list(range(N))))
    Y = list(zip(XY[1::2], list(range(N))))

    X.sort()
    Y.sort()

    edge = []
    for i in range(N - 1):
        edge.append((X[i + 1][0] - X[i][0], X[i][1], X[i + 1][1]))
        edge.append((Y[i + 1][0] - Y[i][0], Y[i][1], Y[i + 1][1]))

    edge.sort()

    uf = UnionFind(N)
    ans = 0
    for d, s, t in edge:
        if not uf.same(s, t):
            uf.union(s, t)
            ans += d

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
