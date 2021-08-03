class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        self.mem = {}

        def dfs(length, lastnum, lastcount):
            if length == n:
                return 1
            if (length, lastnum, lastcount) in self.mem:
                return self.mem[(length, lastnum, lastcount)]
            counts = 0

            for i, nxt in enumerate('123456'):
                if lastnum == nxt:
                    if lastcount < rollMax[i]:
                        counts += dfs(length + 1, nxt, lastcount + 1)
                else:
                    counts += dfs(length + 1, nxt, 1)

            counts = counts % (10**9 + 7)
            self.mem[(length, lastnum, lastcount)] = counts
            return counts

        lastnum = '0'
        lastcount = 0
        res = dfs(0, '0', 0)

        return res
