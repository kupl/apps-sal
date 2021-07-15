class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -1, -1]
        
        for v in nums:
            new_dp = list(dp)
            if dp[v%3] < 0:
                new_dp[v%3] = v
            for i in range(0,3):
                new_i = (i+v) % 3
                if dp[i] >= 0:
                    new_dp[new_i] = max(dp[new_i], dp[i] + v)
                    
            dp = new_dp
#            print(dp)

        return dp[0]
