class Solution:
    def countVowelPermutation(self, n: int) -> int:
        m = {0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0]}
        dp = [1] * 5
        for i in range(1, n):
            dp2 = [0] * 5
            for j in range(5):
                for k in m[j]:
                    dp2[k] += dp[j]
            dp = dp2
        return sum(dp) % (10**9 + 7)
