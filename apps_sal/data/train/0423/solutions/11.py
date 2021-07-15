class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [0] * 40001
        d = 20000
        opt = 0
        for e in arr:
            dp[e+d] = dp[e-difference + d] + 1
            opt = max(opt, dp[e+d])

        return opt         
