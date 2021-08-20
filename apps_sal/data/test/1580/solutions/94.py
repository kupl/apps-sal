class UnionFind:

    def __init__(self, node):
        self.parent = [-1 for _ in range(node)]

    def find(self, target):
        if self.parent[target] < 0:
            return target
        else:
            self.parent[target] = self.find(self.parent[target])
            return self.parent[target]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parent[root_x] > self.parent[root_y]:
            (root_x, root_y) = (root_y, root_x)
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] = root_x

    def get_size(self, x):
        return -self.parent[self.find(x)]

    def get_root(self):
        return [i for (i, root) in enumerate(self.parent) if root < 0]


def main():
    (n, m) = list(map(int, input().split()))
    uf = UnionFind(n)
    for _ in range(m):
        (x, y, _) = [int(x) - 1 for x in input().split()]
        uf.union(x, y)
    print(len(uf.get_root()))


def __starting_point():
    main()


__starting_point()
