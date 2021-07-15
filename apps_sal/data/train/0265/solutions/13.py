class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        dp = [0]*(n+1)
        dict = {}
        dict[0] = 0
        
        curr = 0
        
        for i in range(1,n+1):
            curr += nums[i-1]
            miss = curr - target
            if miss in dict:
                dp[i]= 1 + dp[dict[miss]]
                
            dp[i] = max(dp[i-1],dp[i])
            dict[curr]=i
            
        return dp[n]

