class UnionFind(object):

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.data = [[i] for i in range(n)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        (x, y) = (self.find(x), self.find(y))
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            (x, y) = (y, x)
        self.root[y] = x
        self.size[x] += self.size[y]
        self.data[x].extend(self.data[y])


def main():
    n = int(input())
    uf = UnionFind(n + 1)
    for _ in range(n - 1):
        (x, y) = list(map(int, input().split()))
        uf.union(x, y)
    x = uf.find(1)
    print(*uf.data[x])


def __starting_point():
    main()


__starting_point()
