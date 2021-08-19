class Solution:

    def knightDialer(self, n: int) -> int:
        moveable = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        MOD = 7 + 1000000000.0
        dp = [1] * 10
        for step in range(n - 1):
            newDP = [0] * 10
            for key in range(10):
                for move in moveable[key]:
                    newDP[move] = (newDP[move] + dp[key]) % MOD
            dp = newDP
        return int(sum(dp) % MOD)
