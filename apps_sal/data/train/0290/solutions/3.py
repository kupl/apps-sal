class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def dp(l, r):
            if any(l < c < r for c in cuts):
                ans = r - l + min([dp(l, c) + dp(c, r) for c in cuts if l < c < r], default=0)
                return ans
            return 0
        return dp(0, n)
