class Solution:
    def knightDialer(self, n: int) -> int:

        MOD = 10**9 + 7
        dp = [1] * 10
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        for hop in range(n - 1):
            dp2 = [0] * 10
            for i, move in enumerate(moves):
                count = dp[i]
                for pos in move:
                    dp2[pos] += count
                    dp2[pos] %= MOD
            dp = dp2
        return sum(dp) % MOD
