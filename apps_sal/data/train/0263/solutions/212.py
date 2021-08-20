class Solution(object):

    def knightDialer(self, N):
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for hops in range(N - 1):
            dp2 = [0] * 10
            for (i, c) in enumerate(dp):
                for nei in moves[i]:
                    dp2[i] += dp[nei]
                    dp2[i] %= MOD
            dp = dp2
        return sum(dp) % MOD
