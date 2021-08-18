class Solution:
    def tallestBillboard(self, rods):
        @lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            return max(dp(i + 1, s),
                       dp(i + 1, s - rods[i]) + rods[i],
                       dp(i + 1, s + rods[i]) + rods[i])

        return int(dp(0, 0) / 2)
