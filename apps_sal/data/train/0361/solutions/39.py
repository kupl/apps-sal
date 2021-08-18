class Solution:
    '''def tilingRectangle(self, m, n):
        if m == n:
            return 1
        return self.tilingRectangle(max(m, n) - min(m, n), min(m, n)) + 1'''

    def tilingRectangle(self, m, n):
        self.best = n * m

        def dfs(hts, mvs):
            if mvs >= self.best:
                return
            if all(h == n for h in hts):
                self.best = min(self.best, mvs)
                return
            i = j = min(list(range(m)), key=lambda i: hts[i])
            while j < m and hts[j] == hts[i]:
                j += 1

            for x in range(min(j - i, n - hts[i]), 0, -1):
                dfs(hts[:i] + [hts[i] + x] * x + hts[i + x:], mvs + 1)

        dfs([0] * m, 0)
        return self.best
