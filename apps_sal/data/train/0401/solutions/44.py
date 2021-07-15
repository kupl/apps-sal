class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # # dp = [[0]*3 for _ in range(n)]
        # dp = [0,0,0]
        
#         for i, x in enumerate(nums):
#             m = x % 3
#             if i > 0:
#                 # dp[i] = dp[i-1][::]
#                 # for j in range(3):
#                 #     if dp[i][(j-m)%3] > 0:
#                 #         dp[i][j] = max(dp[i][j], dp[i][(x-m)%3] + x)
#                 rot = [dp[(x-m)%3] for x in range(3)]

#                 for j in range(3):
#                     if rot[j] > 0:
#                         dp[j] = max(dp[j], rot[j] + x) # can add to it
                        
#             dp[m] = max(dp[m], x) # better to start anew with current element
#             # print(i, dp)
                
#         # print(dp)
#         return dp[0]

        seen = [0,0,0]
        for a in nums:
            for i in seen[:]:
                seen[(i+a)%3] = max(seen[(i+a)%3], i+a)
                
            # print(a, seen)
            
        return seen[0]
