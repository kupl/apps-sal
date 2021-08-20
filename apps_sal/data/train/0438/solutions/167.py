class UF:

    def __init__(self, n, m):
        self.p = [i for i in range(n + 1)]
        self.c = [0 for _ in range(n + 1)]
        self.m_cnt = 0
        self.m = m

    def union(self, i, j):
        (pi, pj) = (self.find(i), self.find(j))
        if pi != pj:
            if self.c[pi] == self.m:
                self.m_cnt -= 1
            if self.c[pj] == self.m:
                self.m_cnt -= 1
            self.p[pj] = pi
            self.c[pi] += self.c[pj]
            if self.c[pi] == self.m:
                self.m_cnt += 1

    def mark(self, i):
        self.c[i] = 1
        if self.m == 1:
            self.m_cnt += 1

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        (uf, ans) = (UF(n, m), -1)
        for (i, num) in enumerate(arr, 1):
            uf.mark(num)
            if num - 1 >= 1 and uf.c[num - 1]:
                uf.union(num - 1, num)
            if num + 1 < n + 1 and uf.c[num + 1]:
                uf.union(num + 1, num)
            if uf.m_cnt > 0:
                ans = i
        return ans
