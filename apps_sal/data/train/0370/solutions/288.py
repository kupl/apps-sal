class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = Disj(max(A))
        for a in A:
            for factor in range(2, int(sqrt(a)) + 1):
                if a % factor == 0:
                    dsu.union(a, factor)
                    dsu.union(a, a // factor)
        maxx = 0
        group_count = defaultdict(int)
        for a in A:
            group_id = dsu.find(a)
            group_count[group_id] += 1
            maxx = max(maxx, group_count[group_id])
        return maxx


class Disj(object):

    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

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
