class UnionFind:

    def __init__(self, m, n):
        self.m = m
        self.parents = [i for i in range(n + 1)]
        self.group_size = defaultdict(set)
        self.sizes = defaultdict(int)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        (root_x, root_y) = (self.find(x), self.find(y))
        self.parents[root_x] = root_y
        size_root_x = self.sizes[root_x]
        self.sizes[root_x] = 0
        self.group_size[size_root_x].remove(root_x)
        size_root_y = self.sizes[root_y]
        self.group_size[size_root_y].remove(root_y)
        self.sizes[root_y] = size_root_y + size_root_x
        self.group_size[self.sizes[root_y]].add(root_y)
        if len(self.group_size[self.m]) > 0:
            return True
        else:
            return False


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFind(m, n)
        seen = set()
        res = -1
        for (idx, x) in enumerate(arr):
            seen.add(x)
            uf.sizes[x] = 1
            uf.group_size[1].add(x)
            if x - 1 in seen:
                uf.union(x, x - 1)
            if x + 1 in seen:
                uf.union(x + 1, x)
            if len(uf.group_size[m]) > 0:
                res = idx + 1
        return res
