class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for move in range(1, N + 1):
            for egg in range(1, K + 1):
                dp[move][egg] = dp[move - 1][egg - 1] + dp[move - 1][egg] + 1
            if dp[move][K] >= N:
                return move
