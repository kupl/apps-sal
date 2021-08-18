class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        move_dict = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
                     5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        MOD = 10**9 + 7
        dp = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]

        for i in range(n - 2):
            new_dp = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
            for d in range(10):
                new_dp[d] = sum(dp[move] for move in move_dict[d]) % MOD
            dp = new_dp

        return sum(dp) % MOD
