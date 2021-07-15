class Solution:
    def maxSumDivThree(self, A: List[int]) -> int:
        dp = [0, 0, 0]
        for a in A:
            for i in dp[:]:
                mod = (i + a) % 3
                dp[mod] = max(dp[mod], i + a)
        return dp[0]
        

