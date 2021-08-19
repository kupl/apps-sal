class UnionFind(object):
    __slots__ = ['nodes']

    def __init__(self, n: int) -> None:
        self.nodes = [-1] * n

    def get_root(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.get_root(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> None:
        (root_x, root_y) = (self.get_root(x), self.get_root(y))
        if root_x != root_y:
            (bigroot, smallroot) = (root_x, root_y) if self.nodes[root_x] < self.nodes[root_y] else (root_y, root_x)
            self.nodes[bigroot] += self.nodes[smallroot]
            self.nodes[smallroot] = bigroot


def __starting_point():
    import sys
    n = int(input())
    queries = [tuple(map(int, l.split())) for l in sys.stdin]
    uf = UnionFind(n + 1)
    (get_root, unite) = (uf.get_root, uf.unite)
    groups = {}
    for (x, y) in queries:
        (x_root, y_root) = (get_root(x), get_root(y))
        if x_root not in groups:
            groups[x_root] = [x]
        if y_root not in groups:
            groups[y_root] = [y]
        unite(x, y)
        if x_root == get_root(x):
            groups[x_root].extend(groups[y_root])
        else:
            groups[y_root].extend(groups[x_root])
    print(*groups[get_root(1)])


__starting_point()
