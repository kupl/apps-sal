class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        #[pos, neg]
        dp = [[0,0] for i in range(n)]
        
        if nums[0] > 0:
            dp[0][0] = 1
        elif nums[0] < 0:
            dp[0][1] = 1
        
        #[1,2,3,5,-6,4,0,10]
        # 1 2 3 4 0  
        # 0 0 0 0 5
        
        for i in range(1, n):
            if nums[i] == 0:
                continue
            elif nums[i] > 0:
                if dp[i-1][1] > 0:
                    dp[i][1] = dp[i-1][1]+1
                dp[i][0] = dp[i-1][0]+1
            else:
                if dp[i-1][1] > 0:
                    dp[i][0] = dp[i-1][1]+1
                dp[i][1] = dp[i-1][0]+1
        
        maxLen = 0
        for i in range(n):
            maxLen = max(maxLen, dp[i][0])
            
        return maxLen
            
            
        
        

