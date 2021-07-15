class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n < m:
            n, m = m, n
        if m == n:
            return 1
        heights = [0] * n
        dp = {}
        final = [m * n]
        def helper(heights, counts):
            key = tuple(heights)
            if counts >= final[0]:
                return
            if all(h == m for h in heights):
                final[0] = min(final[0], counts)
                return
            if key in dp and dp[key] <= counts:
                return # dp[key]
            
            dp[key] = counts
            
            min_val = min(heights)
            idx = heights.index(min_val)
            d = 0
            for i in range(idx, n):
                if heights[i] == min_val:
                    d += 1
                else:
                    break
            d = min(m - min_val, d)
            for i in range(d, 0, -1):
                if heights[idx] + i <= m:
                    helper(heights[:idx] + [heights[idx] + i] * i + heights[idx + i:], counts + 1)
                
            return
        helper(heights, 0)
        return final[0]
