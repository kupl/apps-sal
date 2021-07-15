class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [ [0 for _ in range(3)] for _ in range(len(nums))]
        dp[0][nums[0]%3] = nums[0]
        for i in range(1, len(nums)):
            for j in range(3):
                dp[i][j] = dp[i-1][j]
            currNum = nums[i]
            for j in range(3):
                curr = dp[i-1][j] + nums[i]
                k = curr %3
                dp[i][k] = max(dp[i][k], curr)
        return dp[len(nums)-1][0]

