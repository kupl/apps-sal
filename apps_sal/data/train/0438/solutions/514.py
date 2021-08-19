class DS:

    def __init__(self):
        self.intervals = {}
        self.par = {}
        self.all_vals = {}

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def query(self, x):
        px = self.find(x)
        (x, y) = self.intervals[px]
        return y - x + 1

    def add(self, x, m):
        self.par[x] = x
        self.intervals[x] = [x, x]
        if 1 not in self.all_vals:
            self.all_vals[1] = 0
        self.all_vals[1] += 1
        if x + 1 in self.par:
            px = self.find(x)
            py = self.find(x + 1)
            (y1, y2) = self.intervals[py]
            (x1, x2) = self.intervals[px]
            self.par[py] = px
            (x, y) = (min(x1, y1), max(x2, y2))
            self.intervals[px] = [x, y]
            self.all_vals[y2 - y1 + 1] -= 1
            self.all_vals[x2 - x1 + 1] -= 1
            if y - x + 1 not in self.all_vals:
                self.all_vals[y - x + 1] = 0
            self.all_vals[y - x + 1] += 1
        if x - 1 in self.intervals:
            px = self.find(x)
            py = self.find(x - 1)
            (y1, y2) = self.intervals[py]
            (x1, x2) = self.intervals[px]
            self.par[py] = px
            (x, y) = (min(x1, y1), max(x2, y2))
            self.intervals[px] = [x, y]
            self.all_vals[y2 - y1 + 1] -= 1
            self.all_vals[x2 - x1 + 1] -= 1
            if y - x + 1 not in self.all_vals:
                self.all_vals[y - x + 1] = 0
            self.all_vals[y - x + 1] += 1
        return m in self.all_vals and self.all_vals[m] > 0


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        ds = DS()
        ans = -1
        for (i, num) in enumerate(arr):
            if ds.add(num, m):
                ans = i + 1
        return ans
