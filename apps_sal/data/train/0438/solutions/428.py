class dsu:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.len = [1] * n
        self.size = [0] * n
        self.store = [0] * (n + 1)

    def unio(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.len[a] > self.len[b]:
            self.par[b] = a
            self.size[a] += self.size[b]
        elif self.len[a] < self.len[b]:
            self.par[a] = b
            self.size[b] += self.size[a]
        else:
            self.par[b] = a
            self.len[a] += 1
            self.size[a] += self.size[b]

    def find(self, a):
        if a != self.par[a]:
            self.par[a] = self.find(self.par[a])
        return self.par[a]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        ds = dsu(len(arr))
        n = len(arr)
        t = [0] * n
        ans = -1
        tpp = 0
        for i in arr:
            tpp += 1
            curr = i - 1
            t[curr] = 1
            if ds.size[curr] == 0:
                ds.size[curr] = 1
            flag = 0
            if curr >= 1 and t[curr - 1] == 1:
                jm = ds.find(curr - 1)
                ds.store[ds.size[jm]] -= 1
                flag = 1
            if curr < n - 1 and t[curr + 1] == 1:
                jm = ds.find(curr + 1)
                ds.store[ds.size[jm]] -= 1
                flag = 1
            if curr >= 1 and t[curr - 1] == 1:
                ds.unio(curr, curr - 1)
            if curr < n - 1 and t[curr + 1] == 1:
                ds.unio(curr, curr + 1)
            jm = ds.find(curr)
            ds.store[ds.size[jm]] += 1
            if ds.store[m]:
                ans = tpp
        return ans
