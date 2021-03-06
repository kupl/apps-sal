class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 7 + 10 ** 9
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for i in range(n - 1):
            dp2 = [0] * 10
            for (node, count) in enumerate(dp):
                for neighbor in moves[node]:
                    dp2[neighbor] += count
                    dp2[neighbor] %= MOD
            dp = dp2
        return sum(dp) % MOD
