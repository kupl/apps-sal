class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [[0 for _ in range(3)] for _ in range(len(nums)+1)]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        
        for i in range(1, len(nums)+1):
            num = nums[i-1]
            rem = num % 3
            if rem == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0]+num)
                dp[i][1] = max(dp[i-1][1], dp[i-1][1]+num)
                dp[i][2] = max(dp[i-1][2], dp[i-1][2]+num)
            elif rem == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2]+num)
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]+num)
                dp[i][2] = max(dp[i-1][2], dp[i-1][1]+num)
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+num)
                dp[i][1] = max(dp[i-1][1], dp[i-1][2]+num)
                dp[i][2] = max(dp[i-1][2], dp[i-1][0]+num)
        
        return dp[-1][0]
