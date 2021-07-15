class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(dp)):
            dp[i] = [0,0]
        
        ans = 0
        for i, v in enumerate(nums):
            if v > 0:
                dp[i][0] = 1 + dp[i-1][0]
                if dp[i-1][1]: dp[i][1] = 1 + dp[i-1][1]
            if v < 0:
                if dp[i-1][1]:
                    dp[i][0] = 1 + dp[i-1][1]
                dp[i][1] = 1 + dp[i-1][0]
            ans = max(ans, dp[i][0])
        return ans
                    
                
                
                
            
                

