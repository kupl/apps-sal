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
                dp[1][i] = dp[0][i - 1]

            else:
                dp[0][i] = dp[0][i - 1] + 1
                dp[1][i] = dp[1][i - 1] + 1

        return max([i for x in dp for i in x])
