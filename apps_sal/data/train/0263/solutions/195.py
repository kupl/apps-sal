class Solution:

    def knightDialer(self, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(10)]
        next_map = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        MOD = pow(10, 9) + 7
        for i in range(10):
            dp[i][1] = 1
        for k in range(2, n + 1):
            for i in range(10):
                for next_num in next_map[i]:
                    dp[i][k] += dp[next_num][k - 1] % MOD
                    dp[i][k] = dp[i][k] % MOD
        ans = 0
        for i in range(10):
            ans += dp[i][n]
            ans = ans % MOD
        return ans
