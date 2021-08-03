from collections import defaultdict
3
# coding: utf-8


class UnionFind(object):
    def __init__(self, N):
        self.parent = [x for x in range(N)]

    def root(self, x):
        if self.parent[x] == x:
            return x
        return self.root(self.parent[x])

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y

    def num_group(self):
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)


N, M = (int(x) for x in input().split())
B = [[int(x) - 1 for x in input().split()] for _ in range(M)]


def isBridge(nth):
    union_find = UnionFind(N)
    for i in range(M):
        if i == nth:
            continue
        union_find.unite(B[i][0], B[i][1])
    if union_find.num_group() != 1:
        return 1


ret = 0
for i in range(M):
    if isBridge(i):
        ret += 1
print(ret)
