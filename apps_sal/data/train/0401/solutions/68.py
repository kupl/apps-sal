class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*3 for _ in range(n+1)]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        
        print (dp)
        for i in range(1, n+1):
            if nums[i-1] % 3 == 0: # Current remainder == 0
                dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][0] to keep the remainder 0
                dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][1] to keep the remainder 1
                dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][2] to keep the remainder 2
            elif nums[i-1] % 3 == 1: # Current remainder == 1
                dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][2] to keep the remainder 0
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][0] to keep the remainder 1
                dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][1] to keep the remainder 2
            else: # Current remainder == 2
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1]) # Can you tell how this works now?
                dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

        return dp[-1][0]
