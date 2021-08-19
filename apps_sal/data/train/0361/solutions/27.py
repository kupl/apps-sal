class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        self.result = n * m
        heights = [0] * n

        def dfs(cur):
            if cur >= self.result:
                return
            curMinHeight = min(heights)
            if curMinHeight == m:
                self.result = cur
                return
            end = start = heights.index(curMinHeight)
            while end < n and heights[start] == heights[end] and (end - start + 1 + curMinHeight <= m):
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
