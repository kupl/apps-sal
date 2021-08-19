class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for cell in range(n - 1):
            dp2 = [0] * 10
            for (num_cell, count) in enumerate(dp):
                for knight in moves[num_cell]:
                    dp2[knight] += count
                    dp2[knight] %= MOD
                dp = dp2
        return sum(dp) % MOD
