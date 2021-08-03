class Solution:
    def minDifficulty(self, JD: List[int], d: int) -> int:
        n = len(JD)

        @lru_cache(None)
        def dp(i, k):
            if k == 1 and i != n:
                return max(JD[i:])
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return math.inf
            ans = math.inf
            for j in range(i, n):
                ans = min(ans, max(JD[i:j + 1]) + dp(j + 1, k - 1))
            return ans
        return dp(0, d) if dp(0, d) != math.inf else -1
