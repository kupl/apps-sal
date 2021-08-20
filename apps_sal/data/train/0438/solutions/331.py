class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        dsu = DSU()
        used = set()
        ans = -1
        for (index, i) in enumerate(arr):
            if i + 1 in used and dsu.get_count(i + 1) == m or (i - 1 in used and dsu.get_count(i - 1) == m):
                ans = index
            if i + 1 in used:
                dsu.union(i, i + 1)
            if i - 1 in used:
                dsu.union(i, i - 1)
            used.add(i)
        return ans


class DSU:

    def __init__(self):
        self.father = {}
        self.count = {}

    def find(self, a):
        self.father.setdefault(a, a)
        self.count.setdefault(a, 1)
        if a != self.father[a]:
            self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a != _b:
            self.father[_a] = self.father[_b]
            self.count[_b] += self.count[_a]

    def get_count(self, a):
        return self.count[self.find(a)]
