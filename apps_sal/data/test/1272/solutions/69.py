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

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, M = list(map(int, input().split()))
    bridge = [list(map(int, input().split())) for _ in range(M)]

    uf = UnionFind(N)
    ans = [N*(N-1)//2]*M

    for i in range(-1, -1 * M, -1):
        a = bridge[i][0] - 1
        b = bridge[i][1] - 1
        if not uf.same(a, b):
            ans[i-1] = ans[i] - uf.size(a) * uf.size(b)
            uf.union(a, b)
        else:
            ans[i-1] = ans[i]

    for a in ans:
        print(a)


def __starting_point():
    main()

__starting_point()
