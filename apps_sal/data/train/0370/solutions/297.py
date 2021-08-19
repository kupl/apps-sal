class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(max(A))
        for num in A:
            for factor in range(2, int(sqrt(num)) + 1):
                if num % factor == 0:
                    dsu.union(num, factor)
                    dsu.union(num, num // factor)
        max_size = 0
        group_count = {}
        for num in A:
            group_id = dsu.find(num)
            if group_id not in group_count:
                group_count[group_id] = 0
            group_count[group_id] += 1
        return max(group_count.values())


class DSU:

    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1 for i in range(size + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return px
        if self.size[px] > self.size[py]:
            (px, py) = (py, px)
        self.parent[px] = py
        self.size[py] += self.size[px]
        return py
