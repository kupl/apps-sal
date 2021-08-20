import sys


class UnionFind:

    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.parent[x] > self.parent[y]:
                (x, y) = (y, x)
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.cnt -= 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return -self.parent[self.root(x)]

    def get_cnt(self):
        return self.cnt


input = sys.stdin.readline
n = int(input())
s = [set(input()) for i in range(n)]
init_set = set([])
for i in range(n):
    s[i].remove('\n')
    init_set |= s[i]
uf = UnionFind(len(init_set))
to_int = {}
for (i, char) in enumerate(init_set):
    to_int[char] = i
for i in range(n):
    char1 = s[i].pop()
    for char in s[i]:
        (a, b) = (to_int[char1], to_int[char])
        if not uf.is_same(a, b):
            uf.merge(a, b)
print(uf.get_cnt())
