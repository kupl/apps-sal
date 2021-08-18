class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:

        self.best = m * n

        def dfs(heights, count):
            if min(heights) == n:
                self.best = min(self.best, count)
                return
            if count >= self.best:
                return

            min_height = min(heights)
            idx = heights.index(min_height)
            right_end = idx + 1
            while right_end < m and heights[right_end] == min_height:
                right_end += 1
            max_possible_box = min(right_end - idx, n - min_height)

            for box_size in range(max_possible_box, 0, -1):
                new_heights = heights[:]
                for i in range(box_size):
                    new_heights[idx + i] += box_size
                dfs(new_heights, count + 1)

        dfs([0] * m, 0)
        return self.best
