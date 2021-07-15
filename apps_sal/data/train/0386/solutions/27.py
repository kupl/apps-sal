class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = (10 ** 9 + 7)
        vows = 'aeiou'
        mapping = {
            0: [1], # a
            1: [0 ,2], # e
            2: [0, 1, 3, 4], # i
            3: [2, 4], # o
            4: [0] # u
        }
        dp = [[0 for _ in range(len(vows))] for _ in range(n)]
        dp[0] = [1] * len(vows)
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                for next_ch in mapping[j]:
                    dp[i][j] += dp[i - 1][next_ch]
        return sum(dp[-1]) % MOD

