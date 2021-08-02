class UnionFind(object):
    __slots__ = ['nodes']

    def __init__(self, n: int):
        self.nodes = [-1] * n

    def find(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> bool:
        root_x, root_y, nodes = self.find(x), self.find(y), self.nodes

        if root_x != root_y:
            if nodes[root_x] > nodes[root_y]:
                root_x, root_y = root_y, root_x
            nodes[root_x] += nodes[root_y]
            nodes[root_y] = root_x

        return root_x != root_y


def __starting_point():
    import sys
    n = int(input())
    uf = UnionFind(26 + n)
    cc_a = ord('a')
    for i, p in enumerate((l.rstrip() for l in sys.stdin), start=26):
        for cc in list(map(lambda c: ord(c) - cc_a, set(p))):
            uf.unite(i, cc)

    ans = sum(1 for i in range(26, 26 + n) if uf.nodes[i] < 0)
    print(ans)


__starting_point()
