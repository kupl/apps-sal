class DSU:

    def __init__(self):
        self.size = {}
        self.parent = {}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (xp, yp) = (self.find(x), self.find(y))
        if xp == yp:
            return False
        if self.size[xp] < self.parent[yp]:
            (xp, yp) = (yp, xp)
        self.size[xp] += self.size[yp]
        self.parent[yp] = xp
        return True

    def add_node(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def get_size(self, x):
        return self.size[self.find(x)]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        dsu = DSU()
        sizes = collections.Counter()
        ans = -1
        for (i, n) in enumerate(arr, 1):
            dsu.add_node(n)
            for nn in [n - 1, n + 1]:
                if nn in dsu.parent:
                    sizes[dsu.get_size(nn)] -= 1
                    dsu.union(n, nn)
            sizes[dsu.get_size(n)] += 1
            if sizes[m] > 0:
                ans = i
        return ans
