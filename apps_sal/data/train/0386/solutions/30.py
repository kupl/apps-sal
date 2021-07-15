class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n <= 1:
            return n * 5
        start_table = {0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0]}
        dp = [[0] * 5 for i in range(n + 1)]
        for i in range(5):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(5):
                after = start_table[j]
                dp[i][j] = sum(dp[i-1][v] for v in after)
        return sum(dp[-1]) % (10**9 + 7)
