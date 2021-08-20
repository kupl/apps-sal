MOD = 10 ** 9 + 7
num_to_next = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}


class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [1 for _ in range(10)]
        for _ in range(n - 1):
            next_dp = [0 for _ in range(10)]
            for current in range(10):
                for next_pos in num_to_next[current]:
                    next_dp[next_pos] += dp[current]
                    next_dp[next_pos] = next_dp[next_pos] % MOD
            dp = next_dp
        return sum(dp) % MOD
