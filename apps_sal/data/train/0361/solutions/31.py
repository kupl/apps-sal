class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n
        res = n * m

        def dfs(heights, count, rem_area):
            nonlocal res
            if count >= res:
                return

            lowest_idx, lowest_height, width, prev = -1, math.inf, 0, -1
            for i in range(m):
                if heights[i] < lowest_height:
                    lowest_height, lowest_idx, width, prev = heights[i], i, 1, i
                elif heights[i] == lowest_height and prev == i - 1:
                    width, prev = width + 1, i

            if rem_area == 0:
                res = min(res, count)
                return

            width = min(width, n - lowest_height)
            for w in range(width, 0, -1):
                temp = heights.copy()
                for j in range(lowest_idx, lowest_idx + w):
                    temp[j] += w
                dfs(temp, count + 1, rem_area - w * w)

        dfs([0] * m, 0, n * m)
        return res
