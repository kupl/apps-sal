class DSU:

    def __init__(self):
        self.p = {}
        self.size = {}
        self.size_to_node = collections.defaultdict(set)

    def exists(self, x):
        return x in self.p

    def size_exists(self, x):
        return len(self.size_to_node[x]) > 0

    def len(self, x):
        if self.exists(x):
            return self.size[self.find(x)]
        else:
            return -1

    def make_set(self, x):
        self.p[x] = x
        self.size[x] = 1
        self.size_to_node[1].add(x)

    def find(self, x):
        if not self.exists(x):
            return None
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr is None or yr is None:
            return
        self.p[xr] = yr
        self.size_to_node[self.size[yr]].remove(yr)
        self.size_to_node[self.size[xr]].remove(xr)
        self.size[yr] += self.size[xr]
        self.size_to_node[self.size[yr]].add(yr)
        del self.size[xr]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        dsu = DSU()
        latest_group = -1
        for (i, x) in enumerate(arr):
            dsu.make_set(x)
            dsu.union(x, x - 1)
            dsu.union(x, x + 1)
            if dsu.size_exists(m):
                latest_group = i + 1
        return latest_group
