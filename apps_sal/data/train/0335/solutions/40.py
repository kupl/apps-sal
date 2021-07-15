class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dp(i, d):
            if i == n:
                return d == 0, 0
            result = 0
            f, a = dp(i + 1, rods[i] + d)
            if f: result = max(result, a + rods[i])
            f, a = dp(i + 1, d - rods[i])
            if f: result = max(result, a)
            f, a = dp(i + 1, d)
            if f: result = max(result, a)
            return result != 0, result
        
        n = len(rods)
        rods.sort()
        return dp(0, 0)[1]

