from itertools import permutations


class Solution:
    def countOrders(self, n: int) -> int:
        dp = {}
        MOD = 10**9 + 7
        dp[(0, 0)] = 1

        def helper(pick, deliver):
            nonlocal dp
            key = (pick, deliver)
            if key in dp:
                return dp[key]
            elif pick > deliver:
                return 0

            ans = 0
            if pick > 0:
                ans += helper(pick - 1, deliver) * pick % MOD
            if deliver > 0 and pick < deliver:
                ans += helper(pick, deliver - 1) * (deliver - pick) % MOD
            dp[key] = ans
            return ans

        return helper(n, n) % MOD
