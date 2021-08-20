class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        self.res = n * m

        def dfs(heights, moves):
            if min(heights) == m:
                self.res = min(self.res, moves)
                return
            if moves == self.res:
                return
            minh = min(heights)
            left = right = heights.index(minh)
            while right < n and heights[right] == minh:
                right += 1
            for size in range(min(m - minh, right - left), 0, -1):
                newh = heights[:]
                for i in range(size):
                    newh[left + i] += size
                dfs(newh, moves + 1)
        dfs([0] * n, 0)
        return self.res
