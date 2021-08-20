class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5
        mod = 1000000007
        for i in range(n - 1):
            next = [0] * 5
            next[1] += dp[0]
            next[0] += dp[1]
            next[2] += dp[1]
            next[0] += dp[2]
            next[1] += dp[2]
            next[3] += dp[2]
            next[4] += dp[2]
            next[2] += dp[3]
            next[4] += dp[3]
            next[0] += dp[4]
            for j in range(5):
                next[j] = next[j] % mod
            dp = next
        return sum(dp) % mod
