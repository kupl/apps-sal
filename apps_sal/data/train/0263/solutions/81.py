class Solution:
    def knightDialer(self, n: int) -> int:

        mappings = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        mod = 10**9 + 7
        dp = [1] * 10

        for digit in range(2, n + 1):
            dp2 = [0] * 10
            for startNumber, counter in enumerate(dp2):
                for x in mappings[startNumber]:
                    dp2[startNumber] += dp[x]
                    dp2[startNumber]
            dp = dp2
        return sum(dp) % mod
