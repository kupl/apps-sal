class UnionFind:
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]
        self.size = [0 for _ in range(n)]
        self.size_count = [0 for _ in range(n + 1)]
        self.size_count[0] = n

    def init(self, x):
        self.parent[x] = x
        self.size[x] = 1
        self.size_count[1] += 1
        self.size_count[0] -= 1

    def find(self, x):
        if self.parent[x] == -1:
            return -1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return
        if p == -1 or q == -1:
            return
        father, son = p, q
        self.parent[son] = father
        self.size_count[self.size[son]] -= 1
        self.size_count[self.size[father]] -= 1
        self.size[father] += self.size[son]
        self.size_count[self.size[father]] += 1

    def get_size(self, x):
        if self.find(x) == -1:
            return 0
        return self.size[self.find(x)]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFind(n + 1)
        res = -1
        for step, num in enumerate(arr):
            left, right = num - 1, num + 1
            uf.init(num)
            if left >= 1:
                uf.union(left, num)
            if right <= n:
                uf.union(num, right)
            if uf.size_count[m]:
                res = max(res, step + 1)
        return res
