import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


class UnionFind:
    def __init__(self, n: int):
        self.nodes = n
        self.parents = [-1] * n
        self.rank = [0] * n

    # retrun the root of element x
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # unite the group include element x and group include element y
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        else:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # get size of the gourp which element x belongs
    def get_size(self, x):
        return -self.parents[self.find(x)]

    # check if element x and element y is same group
    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, M = [int(i) for i in input().strip().split()]
    links = [None] * M
    for i in range(M):
        links[i] = [int(i) - 1 for i in input().strip().split()]

    u = UnionFind(N)
    ans = list()
    x = N * (N - 1) // 2

    for a, b in links[::-1]:
        ans.append(x)
        if not u.same(a, b):
            x -= u.get_size(a) * u.get_size(b)
        u.unite(a, b)
    return ans


def __starting_point():
    for ans in main()[::-1]:
        print(ans)


__starting_point()
