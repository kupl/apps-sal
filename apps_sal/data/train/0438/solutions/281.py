class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = [i - 1 for i in arr]
        n = len(arr)
        uf = UnionFind(n)
        s = ['0'] * n
        steps = -1
        if m == 1:
            steps = 1
        for i, idx in enumerate(arr):
            s[idx] = '1'
            uf.sz_count[1] += 1
            if idx > 0 and s[idx - 1] == '1':
                uf.find_and_union(idx, idx - 1)
            if idx < n - 1 and s[idx + 1] == '1':
                uf.find_and_union(idx, idx + 1)
            if uf.sz_count[m] > 0:
                steps = i + 1
        return steps


class UnionFind:
    def __init__(self, n):
        self.component_count = n
        self.parents = list(range(n))
        self.size = [1] * n
        self.sz_count = Counter()

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parents[y] = x
        self.sz_count[self.size[x]] -= 1
        self.sz_count[self.size[y]] -= 1
        self.size[x] += self.size[y]
        self.sz_count[self.size[x]] += 1
        self.component_count -= 1

    def find_and_union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 != y0:
            return self.union(x0, y0)
        return 0
