import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)
MOD = 10 ** 9 + 7
INF = float('inf')


class UnionFind:

    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parent = [i for i in range(n_nodes)]
        self.rank = [1] * n_nodes
        self.size = [1] * n_nodes

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

    def get_parent_list(self):
        return [i for i in range(self.n_nodes) if self.find(i) == i]

    def get_n_groups(self):
        return len(self.get_parent_list())

    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def main():
    (N, M) = list(map(int, input().split()))
    edge = [set(map(int, input().split())) for _ in range(M)]
    UF = UnionFind(N)
    for (x, y) in edge:
        UF.unite(x - 1, y - 1)
    parents = UF.get_parent_list()
    answer = 0
    for p in parents:
        size = UF.get_size(p)
        answer = max(answer, size)
    print(answer)


def __starting_point():
    main()


__starting_point()
