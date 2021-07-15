class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0,0,0]
        for i in range(len(nums)):
            for j in dp[:]:
                dp[(j + nums[i])%3] = max(j+nums[i], dp[(j + nums[i])%3])
        return dp[0]

