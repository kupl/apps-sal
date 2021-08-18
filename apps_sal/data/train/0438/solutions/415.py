class DSU:
    def __init__(self, m):
        self.reps = {}
        self.size = {}
        self.m = m
        self.count = 0

    def add(self, x):
        self.reps[x] = x
        self.size[x] = 1
        if self.m == 1:
            self.count += 1

    def find(self, x):
        if not x == self.reps[x]:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]

    def union(self, x, y):
        hX = self.find(x)
        hY = self.find(y)
        if not hX == hY:
            h = min(hX, hY)
            if self.size[hX] == self.m:
                self.count -= 1
            if self.size[hY] == self.m:
                self.count -= 1
            if h == hX:
                self.reps[hY] = h
                self.size[hX] += self.size[hY]
                if self.size[hX] == self.m:
                    self.count += 1
                self.size.pop(hY)
            else:
                self.reps[hX] = h
                self.size[hY] += self.size[hX]
                if self.size[hY] == self.m:
                    self.count += 1
                self.size.pop(hX)


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dsu, s = DSU(m=m), -1
        for i, x in enumerate(arr):
            dsu.add(x)
            if x - 1 in dsu.reps:
                dsu.union(x - 1, x)
            if x + 1 in dsu.reps:
                dsu.union(x + 1, x)
            if dsu.count > 0:
                s = max(s, i + 1)
        return s
