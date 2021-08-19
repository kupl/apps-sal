class Solution:
    '''def tilingRectangle(self, m, n):
        # greedy approach doesnt work mofo
        if m == n:
            return 1
        return self.tilingRectangle(max(m, n) - min(m, n), min(m, n)) + 1'''

    def tilingRectangle(self, m, n):
        self.best = n * m

        def dfs(heights, mvs):
            # if moves are going over out best just STOP
            if mvs >= self.best:
                return

            # if all items in
            if all(h == n for h in heights):
                self.best = min(self.best, mvs)
                return
            i = j = min(list(range(m)), key=lambda i: heights[i])
            while j < m and heights[j] == heights[i]:
                j += 1

            for x in range(min(j - i, n - heights[i]), 0, -1):
                dfs(heights[:i] + [heights[i] + x] * x + heights[i + x:], mvs + 1)

        heights = [0] * m
        dfs(heights, 0)
        return self.best
