class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        dp = {}
        mod = 10**9 + 7
        for a in A:
            dp[a] = 1
            for b in A:
                if a % b == 0 and b in dp and a // b in dp:
                    dp[a] += dp[b] * dp[a // b]
                    dp[a] %= mod

        return sum(dp.values()) % mod
