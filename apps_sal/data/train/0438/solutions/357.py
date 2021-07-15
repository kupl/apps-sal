class UF:
    def __init__(self, n):
        self.p = [-1 for _ in range(n+1)]
        self.size = [0 for _ in range(n+1)]
        
    def find(self, x):
        if self.p[x] == -1:
            return -1
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        self.p[pa] = pb
        self.size[pb] += self.size[pa]
        
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UF(len(arr))
        ans = -1

        for i, x in enumerate(arr):
            uf.p[x] = x
            uf.size[x] = 1

            if x > 0 and uf.find(x - 1) != -1:
                if uf.size[uf.find(x-1)] == m:
                    ans = i
                uf.union(x, x-1)

            if x < n and uf.find(x + 1) != -1:
                if uf.size[uf.find(x+1)] == m:
                    ans = i
                uf.union(x, x+1)
            if uf.size[uf.find(x)] == m:
                ans = i+1

        return ans


