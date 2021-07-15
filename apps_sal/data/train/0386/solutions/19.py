class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = (10**9 + 7)
        mapping = [
            [1,2,4], [0, 2], [1, 3], [2], [2, 3]
        ]
        dp = [[0 for _ in range(5)] for _ in range(n)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = 1
                    continue
                for prev in mapping[j]:
                    dp[i][j] += dp[i - 1][prev]
        return sum(dp[n - 1]) % MOD
