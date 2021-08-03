class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.ans = n * m

        def helper(heights, moves):
            if all(height == n for height in heights):
                self.ans = min(self.ans, moves)
                return None

            if moves >= self.ans:
                return None

            min_height = min(heights)
            min_height_idx = heights.index(min_height)

            right_idx = min_height_idx + 1

            while right_idx < m and heights[right_idx] == min_height:
                right_idx += 1

            for idx in range(min(n - min_height, right_idx - min_height_idx), -1, -1):
                new_heights = heights[:]

                for next_idx in range(idx):
                    new_heights[min_height_idx + next_idx] += idx

                helper(new_heights, moves + 1)

        helper([0] * m, 0)
        return self.ans
