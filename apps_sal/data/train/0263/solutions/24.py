class Solution:

    def knightDialer(self, N: int) -> int:
        dic = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        dp = [1 for i in range(10)]
        for i in range(N - 1):
            new_dp = [0 for j in range(10)]
            for j in range(10):
                for k in dic[j]:
                    new_dp[j] += dp[k]
                new_dp[j] %= 10 ** 9 + 7
            dp = new_dp
        return sum(dp) % (10 ** 9 + 7)
