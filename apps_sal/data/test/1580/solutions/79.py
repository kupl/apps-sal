class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False

        if self.data[x] < self.data[y]:
            x, y = y, x

        self.data[y] += self.data[x]
        self.data[x] = y
        return True

    def root(self, x):
        if self.data[x] < 0:
            return x
        self.data[x] = self.root(self.data[x])
        return self.data[x]

    def size(self, x):
        return -self.data[self.root(x)]


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for i in range(M):
        x, y, z = map(int, input().split())
        uf.merge(x - 1, y - 1)

    cnt = 0
    for i in range(N):
        if uf.root(i) == i:
            cnt += 1

    print(cnt)


def __starting_point():
    main()


__starting_point()
