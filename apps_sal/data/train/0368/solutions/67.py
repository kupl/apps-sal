class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @lru_cache(None)
        def dp(i, k):
            if i == len(satisfaction):
                return 0
            return max(dp(i + 1, k), dp(i + 1, k + 1) + satisfaction[i] * k)
        return dp(0, 1)
