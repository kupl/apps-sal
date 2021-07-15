class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        
        for num in nums:
            r = num % 3
            
            pre = dp[:]
            for i in range(3):
                if pre[i]:
                    dp[(i + r) % 3] = max(pre[(i + r) % 3], pre[i] + num)
                    
            if dp[r] == 0:
                dp[r] = num
                
        return dp[0]

