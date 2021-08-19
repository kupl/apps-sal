class Solution:

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        r1 = self.find(a)
        r2 = self.find(b)
        if r1 == r2:
            return
        if self.size[r1] == self.m:
            self.num_m -= 1
        if self.size[r2] == self.m:
            self.num_m -= 1
        ns = self.size[r1] + self.size[r2]
        if ns == self.m:
            self.num_m += 1

        if self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
            self.size[r1] = ns
        else:
            if self.rank[r2] > self.rank[r1]:
                self.parent[r1] = r2
                self.size[r2] = ns
            else:
                self.parent[r1] = r2
                self.rank[r2] += 1
                self.size[r2] = ns

    def findLatestStep(self, arr: List[int], m: int) -> int:
        self.parent = {}
        self.rank = {}
        self.size = {}
        self.m = m
        self.num_m = 0
        ans = -1
        for i, v in enumerate(arr):
            self.parent[v] = v
            self.rank[v] = 1
            self.size[v] = 1
            if self.size[v] == m:
                self.num_m += 1
            if v - 1 in self.parent:
                self.union(v - 1, v)
            if v + 1 in self.parent:
                self.union(v + 1, v)
            if self.num_m > 0:
                ans = i + 1
            # print(i,self.num_m,ans)
        return ans
