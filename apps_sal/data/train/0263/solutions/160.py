class Solution:
    def knightDialer(self, n: int) -> int:

        N = n
        l = 10
        dp = [1] * l
        m = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        for _ in range(2, N + 1):
            dp2 = [0] * l
            for i in range(l):
                for j in m[i]:
                    dp2[i] += dp[j]
            dp = dp2

        return sum(dp) % (10**9 + 7)
