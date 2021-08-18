class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        uf = UnionFindHelper()
        res = -1
        for i, curr in enumerate(arr):
            uf.add(curr)
            step = i + 1
            for neighbor in [curr - 1, curr + 1]:
                if uf.contains(neighbor):
                    if uf.getrank(neighbor) == m:
                        res = step - 1
                    uf.union(neighbor, curr)
        return res


class UnionFindHelper:
    def __init__(self):
        self.parent = {}
        self.ranks = {}
        self.count = 0

    def contains(self, item):
        return item in self.parent

    def add(self, item):
        if item not in self.parent:
            self.parent[item] = item
            self.ranks[item] = 1
            self.count += 1

    def getrank(self, item):
        return self.ranks[self.find(item)]

    def find(self, item):
        if item != self.parent[item]:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1, item2):
        item1 = self.find(item1)
        item2 = self.find(item2)
        rank1 = self.ranks[item1]
        rank2 = self.ranks[item2]
        if item1 != item2:
            self.parent[item1] = item2
            self.ranks[item2] = rank1 + rank2
            self.count -= 1
