class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0,0,0]
        for num in nums:
            for idx in dp[:]:
                dp[(idx+num)%3] = max(dp[(idx+num)%3], idx+num)
        return dp[0]
