class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        from functools import lru_cache

        @lru_cache(None)
        def helper(i=0, j=n):
            ans = math.inf
            for c in cuts:
                if c <= i:
                    continue
                if c >= j:
                    break
                ans = min(ans, j - i + helper(i, c) + helper(c, j))
            if ans == math.inf:
                return 0
            return ans
        return helper()
