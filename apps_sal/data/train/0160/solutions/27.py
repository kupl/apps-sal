class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2 :
            return True
        dp = [[0]*n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-1):
            dp[i][i+1] = max(nums[i],nums[i+1])
            
        for j in range(2,n):
            for i in range(n-j):
                dp[i][j+i] = max(nums[i]+min(dp[i+1][j+i-1],dp[i+2][j+i]), nums[j+i] + min(dp[i][j+i-2],dp[i+1][j+i-1]))
        #print(dp)
        if sum(nums) - dp[0][n-1] > dp[0][n-1]:
            return False
        return True
