class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(l)]
        res = 0
        if nums[0] > 0:
            dp[0][0] = 1
            res = 1
        if nums[0] < 0:
            dp[0][1] = 1
        
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur > 0:
                if dp[i-1][0] == 0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = dp[i-1][0] + 1
                
                if dp[i-1][1] != 0:
                    dp[i][1] = dp[i-1][1] + 1
                    
            if cur < 0:
                if dp[i-1][0] == 0:
                    dp[i][1] = 1
                else:
                    dp[i][1] = dp[i-1][0] + 1
                
                if dp[i-1][1] != 0:
                    dp[i][0] = dp[i-1][1] + 1
            
            res = max(res, dp[i][0])
        
        return res
