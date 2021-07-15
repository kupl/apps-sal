class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        @lru_cache(None)
        def helper(heights):
            mh = min(heights)
            if mh == n:
                return 0
            
            ret = float('inf')
            j = heights.index(mh)
            w = 1
            while mh + w <= n and j + w - 1 < m and heights[j + w - 1] == mh:
                ret = min(ret, 1 + helper(heights[:j] + (mh + w,) * w + heights[j + w:]))
                w += 1
            
            return ret
            
        return helper((0,) * m)

