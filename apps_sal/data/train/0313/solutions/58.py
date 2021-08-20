class UnionFind:

    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        (fx, fy) = (self.find(x), self.find(y))
        if fx == fy:
            return
        self.father[fx] = fy
        self.size[fy] += self.size[fx]

    def get_size(self, x):
        fx = self.find(x)
        return self.size[fx]


class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        sort_indexes = sorted(range(n), key=lambda i: bloomDay[i])
        uf = UnionFind(n)
        bouquets = 0
        bloomed = [False] * n
        for idx in sort_indexes:
            bloomed[idx] = True
            (left, right) = (idx - 1, idx + 1)
            (left_size, right_size) = (0, 0)
            if left >= 0 and bloomed[left]:
                left_size = uf.get_size(left)
                uf.union(left, idx)
            if right <= n - 1 and bloomed[right]:
                right_size = uf.get_size(right)
                uf.union(right, idx)
            cur_size = uf.get_size(idx)
            bouquets += cur_size // k - (left_size // k + right_size // k)
            if bouquets >= m:
                return bloomDay[idx]
        return -1
