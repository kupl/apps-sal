class UnionFind:

    def __init__(self):
        self.parents = {}
        self.size = {}
        self.counts = defaultdict(int)

    def add(self, val):
        self.parents[val] = val
        self.size[val] = 1
        self.counts[1] += 1

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        if not u in self.parents or not v in self.parents:
            return
        pU = self.find(u)
        pV = self.find(v)
        if pU == pV:
            return
        self.counts[self.size[pU]] -= 1
        self.counts[self.size[pV]] -= 1
        if self.size[pU] < self.size[pV]:
            self.parents[pU] = self.parents[pV]
            self.size[pV] += self.size[pU]
            self.counts[self.size[pV]] += 1
        else:
            self.parents[pV] = self.parents[pU]
            self.size[pU] += self.size[pV]
            self.counts[self.size[pU]] += 1


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = UnionFind()
        iter = 1
        res = -1
        for num in arr:
            uf.add(num)
            uf.union(num, num - 1)
            uf.union(num, num + 1)
            if uf.counts[m] > 0:
                res = iter
            iter += 1
        return res
