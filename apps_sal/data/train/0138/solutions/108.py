class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        dp = [0,0] # [+,-]
        for i, n in enumerate(nums):
            if n == 0:
                dp = [0, 0]
                continue
            
            if n < 0:
                dp = [0 if dp[1] == 0 else (dp[1] + 1), dp[0] + 1]
            else:
                dp = [dp[0] + 1, 0 if dp[1] == 0 else (dp[1] + 1)]
            ans = max(ans, dp[0])
        
        return ans
