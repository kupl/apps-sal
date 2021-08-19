class Solution:

    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] * 5
        foll = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        for _ in range(1, n):
            tmp = [0] * 5
            for (idx, follow) in enumerate(foll):
                for i in follow:
                    tmp[idx] += dp[i]
                    tmp[idx] %= MOD
            dp = tmp
        return sum(dp) % MOD
