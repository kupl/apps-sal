class UnionFind:

    def __init__(self):
        self.sets = {}
        self.size = {}
        self.sizes = collections.defaultdict(int)

    def make_set(self, s):
        self.sets[s] = s
        self.size[s] = 1
        self.sizes[1] += 1

    def find(self, s):
        if self.sets[s] != s:
            self.sets[s] = self.find(self.sets[s])
        return self.sets[s]

    def union(self, s1, s2):
        (a, b) = (self.find(s1), self.find(s2))
        if a == b:
            return
        self.sizes[self.size[a]] -= 1
        self.sizes[self.size[b]] -= 1
        if self.sizes[self.size[a]] == 0:
            self.sizes.pop(self.size[a], None)
        if self.sizes[self.size[b]] == 0:
            self.sizes.pop(self.size[b], None)
        self.sets[a] = b
        self.size[b] += self.size[a]
        self.sizes[self.size[b]] += 1

    def get_size(self, m):
        return m in self.sizes


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        seen = set()
        uf = UnionFind()
        res = -1
        for (i, v) in enumerate(arr, 1):
            uf.make_set(v)
            if v + 1 in seen:
                uf.union(v, v + 1)
            if v - 1 in seen:
                uf.union(v, v - 1)
            seen.add(v)
            if uf.get_size(m):
                res = i
        return res
