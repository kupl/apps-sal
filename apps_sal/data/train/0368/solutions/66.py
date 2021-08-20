class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        import functools

        @functools.lru_cache(None)
        def DP(i, j):
            if i == n:
                return 0
            return max(satisfaction[i] * j + DP(i + 1, j + 1), DP(i + 1, j))
        return DP(0, 1)
