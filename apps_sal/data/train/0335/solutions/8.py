from functools import lru_cache
from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # Dynamic Programming
        # Let dp[i][s] be the largest score we can get using rods[j] (j >= i),
        # after previously writing a sum of s.
        # Time  complexity: O(N x S), where N is the length of rods and S is the maximum of sum(rods).
        # Space complexity: O(N x S)
        # @lru_cache(None)
        # def dp(i, s):
        #     if i == len(rods):
        #         return 0 if s == 0 else float(\"-inf\")
        #     return max(dp(i + 1, s),
        #                dp(i + 1, s - rods[i]),
        #                dp(i + 1, s + rods[i]) + rods[i])
        # return dp(0, 0)

        # dp[d] mean the maximum pair of sum we can get with pair difference d
        # For example, if have a pair of sum (a, b) with a > b, then dp[a - b] = b
        # If we have dp[diff] = a, it means we have a pair of sum (a, a + diff).
        # And this is the biggest pair with difference = a
        dp = defaultdict(int)
        dp[0] = 0
        for x in rods:
            for d, y in list(dp.copy().items()):
                dp[d + x] = max(dp[d + x], y)
                dp[abs(d - x)] = max(dp[abs(d - x)], y + min(d, x))
        return dp[0]
