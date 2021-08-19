class Solution:

    def knightDialer(self, N: int) -> int:
        parent_child_dict = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        dp = [[0] * 10 for _ in range(N)]
        for j in range(10):
            dp[0][j] = 1
        for i in range(N - 1):
            for j in range(10):
                children = parent_child_dict[j]
                for child in children:
                    dp[i + 1][child] += dp[i][j]
                dp[i][j] = dp[i][j] % (10 ** 9 + 7)
        return sum(dp[N - 1]) % (10 ** 9 + 7)
