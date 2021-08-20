class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = n * m

        def dp(heights, n_square):
            if n_square > self.best:
                return
            if heights == [n] * m:
                self.best = min(self.best, n_square)
            min_index = min(range(m), key=lambda x: heights[x])
            (i, j) = (min_index, min_index)
            while j < m and heights[i] == heights[j]:
                j += 1
            max_line = min(j - i + int(j == m), n - heights[i])
            result = float('inf')
            for x in range(max_line, 0, -1):
                cur = dp(heights[:i] + [heights[i] + x] * x + heights[i + x:], n_square + 1)
                if cur:
                    result = min(result, cur)
            return result
        dp([0] * m, 0)
        return self.best
