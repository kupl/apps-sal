import sys
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


class UnionFind:

    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def get_size(self, x):
        return -self.parents[self.find(x)]

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_parent_list(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def main():
    (N, K, L) = map(int, input().split())
    tree_road = UnionFind(N)
    tree_subway = UnionFind(N)
    for _ in range(K):
        (p, q) = map(int, input().split())
        p -= 1
        q -= 1
        tree_road.unite(p, q)
    for _ in range(L):
        (r, s) = map(int, input().split())
        r -= 1
        s -= 1
        tree_subway.unite(r, s)
    d = {}
    for i in range(N):
        p1 = tree_road.find(i)
        p2 = tree_subway.find(i)
        if (p1, p2) not in d:
            d[p1, p2] = 1
        else:
            d[p1, p2] += 1
    for i in range(N):
        p1 = tree_road.find(i)
        p2 = tree_subway.find(i)
        print(d[p1, p2], end=' ')


def __starting_point():
    main()


__starting_point()
