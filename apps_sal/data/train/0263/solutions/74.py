class Solution:

    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        nxt_pos = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1 for _ in range(10)]
        for _ in range(1, n):
            new_dp = [0 for _ in range(10)]
            for (val, times) in enumerate(dp):
                for i in nxt_pos[val]:
                    new_dp[i] += times
                    new_dp[i] %= mod
            dp = new_dp
        return sum(dp) % mod
