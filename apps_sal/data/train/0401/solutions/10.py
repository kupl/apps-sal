class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[0]*3 for _ in range(n)]
        
        for i, x in enumerate(nums):
            m = x % 3
            if i > 0:
                dp[i] = dp[i-1][::]
                # for j in range(3):
                #     if dp[i][(j-m)%3] > 0:
                #         dp[i][j] = max(dp[i][j], dp[i][(x-m)%3] + x)
                rot = [dp[i][(x-m)%3] for x in range(3)]

                for j in range(3):
                    if rot[j] > 0:
                        dp[i][j] = max(dp[i][j], rot[j] + x) # can add to it
                        
            dp[i][m] = max(dp[i][m], x) # better to start anew with current element
            
                
        print(dp)
        return dp[-1][0]
