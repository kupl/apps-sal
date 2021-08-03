import sys
from collections import Counter as cc
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0] * n

    def get_root(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]

    def unite(self, i, j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j:
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1

    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False


def main():
    n, m, k = mi()
    e = [0] * n
    uf = UnionFind(n)
    for i in range(m):
        a, b = mi()
        a -= 1
        b -= 1
        e[a] -= 1
        e[b] -= 1
        uf.unite(a, b)

    for _ in range(k):
        a, b = mi()
        a -= 1
        b -= 1
        if uf.is_in_group(a, b):
            e[a] -= 1
            e[b] -= 1

    for i in range(n):
        uf.get_root(i)
    s = cc(uf.parent)
    for i in range(n):
        x = uf.get_root(i)
        e[i] += s[x] - 1
    print(*e)


def __starting_point():
    main()


__starting_point()
