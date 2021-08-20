class Solution:

    def countVowelPermutation(self, n: int) -> int:
        if n <= 1:
            return n * 5
        end_table = {0: [1, 2, 4], 1: [0, 2], 2: [1, 3], 3: [2], 4: [2, 3]}
        dp = [[0] * 5 for i in range(n + 1)]
        for i in range(5):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(5):
                before = end_table[j]
                dp[i][j] = sum((dp[i - 1][v] for v in before))
        return sum(dp[-1]) % (10 ** 9 + 7)
