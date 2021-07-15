class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        
        n = len(nums)+1
        
        dp = [[0]*3 for i in range(n)]
        
        dp[0][0], dp[0][1], dp[0][2] = 0, -float('inf'), -float('inf')
        
        for i in range(1,n):
            
            rem = nums[i-1]%3
            
            if rem == 0:
                
                dp[i][0] = dp[i-1][0] + nums[i-1]
                dp[i][1] = dp[i-1][1] + nums[i-1]
                dp[i][2] = dp[i-1][2] + nums[i-1]
                
            elif rem == 1:
                
                dp[i][0] = max(dp[i-1][0],dp[i-1][2]+nums[i-1])
                dp[i][1] = max(dp[i-1][1],dp[i-1][0]+nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1]+nums[i-1])
                
            else:
                
                dp[i][0] = max(dp[i-1][0],dp[i-1][1]+nums[i-1])
                dp[i][1] = max(dp[i-1][1],dp[i-1][2]+nums[i-1])
                dp[i][2] = max(dp[i-1][2],dp[i-1][0]+nums[i-1])
                
        return dp[-1][0]
