class Solution:

    def knightDialer(self, n: int) -> int:
        valid_moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        m = 10 ** 9 + 7
        for _ in range(n - 1):
            new_dp = [0] * 10
            for i in range(10):
                for j in valid_moves[i]:
                    new_dp[j] += dp[i] % m
            dp = new_dp
        return sum(dp) % m
