class DSU:
    def __init__(self, n):
        self.r = collections.defaultdict(int)
        self.p = collections.defaultdict(int)
        self.s = collections.defaultdict(int)
        self.scount = collections.defaultdict(int)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if self.r[px] > self.r[py]:
            self.p[py] = px
            self.scount[self.s[py]] -= 1
            self.scount[self.s[px]] -= 1
            self.s[px] += self.s[py]
            self.s[py] = 0
            self.scount[self.s[px]] += 1

        if self.r[px] < self.r[py]:
            self.p[px] = py
            self.scount[self.s[py]] -= 1
            self.scount[self.s[px]] -= 1
            self.s[py] += self.s[px]
            self.s[px] = 0
            self.scount[self.s[py]] += 1
        else:
            self.p[py] = px
            self.scount[self.s[py]] -= 1
            self.scount[self.s[px]] -= 1
            self.r[px] += 1
            self.s[px] += self.s[py]
            self.s[py] = 0
            self.scount[self.s[px]] += 1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dsu = DSU(len(arr))
        seen = set()
        ret = -1
        for i in range(len(arr)):
            dsu.p[arr[i]] = arr[i]
            dsu.s[arr[i]] = 1
            dsu.r[arr[i]] = 0
            dsu.scount[1] += 1
            if arr[i] + 1 in seen:
                dsu.union(arr[i], arr[i] + 1)
            if arr[i] - 1 in seen:
                dsu.union(arr[i], arr[i] - 1)

            if dsu.scount[m] > 0:
                ret = max(ret, i)
            seen.add(arr[i])

        return ret + 1 if ret != -1 else -1
