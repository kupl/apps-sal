class Solution:
    def knightDialer(self, N: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        MOD = 10**9 + 7
        for i in range(N - 1):
            next_dp = [0] * 10
            for j in range(10):
                for next_digit in moves[j]:
                    next_dp[j] = (next_dp[j] + dp[next_digit]) % MOD
            dp = next_dp
        return sum(dp) % MOD
