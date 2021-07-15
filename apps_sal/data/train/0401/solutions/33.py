class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for n in nums:
            if n % 3 == 0:
                dp0 = dp[0] + n
                if dp[1] > 0: dp1 = dp[1] + n
                else: dp1 = dp[1]
                if dp[2] > 0: dp2 = dp[2] + n
                else: dp2 = dp[2]
            elif n % 3 == 1:
                if dp[2] > 0: dp0 = max(dp[0], dp[2] + n)
                else: dp0 = dp[0]
                if dp[0] > 0: dp1 = max(dp[1], dp[0] + n)
                else: dp1 = max(dp[1], n) 
                if dp[1] > 0: dp2 = max(dp[2], dp[1] + n)
                else: dp2 = dp[2]
            elif n % 3 == 2:
                if dp[1] > 0: dp0 = max(dp[0], dp[1] + n)
                else: dp0 = dp[0]
                if dp[2] > 0: dp1 = max(dp[1], dp[2] + n)
                else: dp1 = dp[1]
                if dp[0] > 0: dp2 = max(dp[2], dp[0] + n)
                else: dp2 = max(dp[2], n)
            dp[0] = dp0
            dp[1] = dp1
            dp[2] = dp2
            

        return dp[0]

