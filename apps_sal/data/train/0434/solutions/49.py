class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        DP
        '''

        n = len(nums)
        if sum(nums) == n:
            return n - 1

        dp = [[0 for x in range(len(nums))] for y in range(2)]

        dp[0][0] = 1 if nums[0] == 1 else 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[0][i] = 0
                # basically \"takes\" the previous run of ones
                dp[1][i] = dp[0][i - 1]

            else:
                dp[0][i] = dp[0][i - 1] + 1
                dp[1][i] = dp[1][i - 1] + 1

        # print(dp)
        return max([i for x in dp for i in x])


#         '''
#         sliding window
#         '''

#         previousRun = 0
#         currentRun = 0
#         best = 0
#         sawZero = False


#         for n in nums:
#             if n == 0:
#                 previousRun = currentRun
#                 currentRun = 0
#                 sawZero = True
#             else:
#                 currentRun += 1
#                 best = max(best, previousRun+currentRun)
#         if sawZero == False:
#             best -= 1
#         return best
