class Subset:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        if self.rank[u] > self.rank[v]:
            self.parent[v] = self.find(u)
        if self.rank[v] > self.rank[u]:
            self.parent[u] = self.find(v)
        if self.rank[u] == self.rank[v]:
            self.parent[v] = self.find(u)
            self.rank[u] += self.rank[v]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        subset = Subset(n)
        ls = [0] * n
        size = [1] * n
        res = -1
        cnt = 0
        for i in range(n):
            idx = arr[i] - 1
            ls[idx] = 1
            sizeMiddle = 1
            if idx > 0:
                if ls[idx - 1] == 1:
                    p = subset.find(idx - 1)
                    sizeLeft = size[p]
                    subset.union(min(idx, p), max(idx, p))
                    if sizeLeft == m:
                        cnt -= 1
                    sizeMiddle += sizeLeft
            if idx < n - 1:
                if ls[idx + 1] == 1:
                    p2 = subset.find(idx + 1)
                    sizeRight = size[p2]
                    subset.union(min(idx, p2), max(idx, p2))
                    if sizeRight == m:
                        cnt -= 1
                    sizeMiddle += sizeRight
            finalP = subset.find(idx)
            size[finalP] = sizeMiddle
            if sizeMiddle == m:
                cnt += 1
            if cnt > 0:
                res = max(res, i + 1)
        return res
