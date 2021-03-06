class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:

        @lru_cache(None)
        def dp(i, d):
            if i == n:
                return 0 if d == 0 else -1
            result = -1
            a = dp(i + 1, rods[i] + d)
            if a >= 0:
                result = max(result, a + rods[i])
            a = dp(i + 1, d - rods[i])
            if a >= 0:
                result = max(result, a)
            a = dp(i + 1, d)
            if a >= 0:
                result = max(result, a)
            return result
        n = len(rods)
        rods.sort()
        return dp(0, 0)
