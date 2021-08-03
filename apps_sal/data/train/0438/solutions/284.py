class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def get_size(self, x):
        return self.sz[self.find(x)]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        dsu = DSU(n)
        cur_string = [0] * n
        ans = -1
        cur_m_count = 0
        for step_0indexed, pos_1indexed in enumerate(arr):
            pos_to_be1 = pos_1indexed - 1
            cur_string[pos_to_be1] = 1
            if pos_to_be1 >= 1 and cur_string[pos_to_be1 - 1] == 1:
                if dsu.get_size(pos_to_be1 - 1) == m:
                    cur_m_count -= 1
                dsu.union(pos_to_be1, pos_to_be1 - 1)
            if pos_to_be1 < n - 1 and cur_string[pos_to_be1 + 1] == 1:
                if dsu.get_size(pos_to_be1 + 1) == m:
                    cur_m_count -= 1
                dsu.union(pos_to_be1, pos_to_be1 + 1)

            if dsu.get_size(pos_to_be1) == m:
                cur_m_count += 1
            if cur_m_count > 0:
                ans = step_0indexed + 1
        return ans
