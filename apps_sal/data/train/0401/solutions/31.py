class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, None, None]
        for num in nums:
            mod = num % 3
            if mod == 0:
                dp[0], dp[1], dp[2] = (dp[0] + num,
                                       dp[1] + num if dp[1] else None,
                                       dp[2] + num if dp[2] else None)
            elif mod == 1:
                dp[0], dp[1], dp[2] = (max(dp[0], dp[2] + num if dp[2] else 0),
                                       max(dp[1] if dp[1] else 0, dp[0] + num),
                                       max(dp[2] if dp[2] else 0, dp[1] + num if dp[1] else 0) if dp[1] or dp[2] else None)
            elif mod == 2:
                dp[0], dp[1], dp[2] = (max(dp[0], dp[1] + num if dp[1] else 0),
                                       max(dp[1] if dp[1] else 0, dp[2] + num if dp[2] else 0) if dp[1] or dp[2] else None,
                                       max(dp[2] if dp[2] else 0, dp[0] + num))
        return dp[0]
