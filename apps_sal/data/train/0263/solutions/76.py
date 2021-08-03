class Solution:
    def knightDialer(self, n: int) -> int:
        res = 0
        path = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        dp = [1] * 10
        MOD = 10**9 + 7

        for i in range(2, n + 1):
            dp2 = [0] * 10
            for j in range(10):
                for p in path[j]:
                    dp2[j] += dp[p]
                # dp[j] %= MOD
            dp = dp2
        res = sum(dp)

        return res % MOD
