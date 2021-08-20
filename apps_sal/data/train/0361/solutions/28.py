class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            return self.tilingRectangle(m, n)
        self.result = n * m
        heights = [0] * m

        def dfs(cur):
            if cur >= self.result:
                return
            curMinHeight = min(heights)
            if curMinHeight == n:
                self.result = cur
                return
            end = start = heights.index(curMinHeight)
            while end < m and heights[start] == heights[end] and (end - start + 1 + curMinHeight <= n):
                end += 1
            for i in range(end - 1, start - 1, -1):
                size = i - start + 1
                for j in range(start, i + 1):
                    heights[j] += size
                dfs(cur + 1)
                for j in range(start, i + 1):
                    heights[j] -= size
        dfs(0)
        return self.result
