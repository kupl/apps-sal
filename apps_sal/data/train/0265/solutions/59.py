class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefixSum = {0: -1}
        dp = [0] * len(nums)

        currSum = 0
        for i in range(len(nums)):
            currSum = currSum + nums[i]
            if currSum - target in prefixSum:
                end = prefixSum[currSum - target]
                dp[i] = max(1 + dp[end], dp[i - 1])
            elif i == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
            prefixSum[currSum] = i
        return dp[len(nums) - 1]
