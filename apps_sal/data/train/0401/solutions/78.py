class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [[0 for j in range(3)] for i in range(n)]
        # dp[0][nums[0]%3] = nums[0]
        # for i in range(1, n):
        #     for j in range(3):
        #         dp[i][j] = dp[i-1][j]
        #         if (j-nums[i]) % 3 == 0:
        #             dp[i][j] = max(dp[i-1][(j-nums[i]) % 3] + nums[i], dp[i-1][j])
        #         else:
        #             if dp[i-1][(j-nums[i]) % 3] > 0:
        #                 dp[i][j] = max(dp[i-1][(j-nums[i]) % 3] + nums[i], dp[i-1][j])
        # # print([i[0] for i in dp])
        # # print([i[1] for i in dp])
        # # print([i[2] for i in dp])
        # return dp[n-1][0]
        
        dp = [[0 for j in range(3)] for i in range(n+1)]
        dp[0][0], dp[0][1], dp[0][2] = 0, -float('inf'), -float('inf')
        for i in range(1, n+1):
            for j in range(3):
                dp[i][j] = max(dp[i-1][(j-nums[i-1]) % 3] + nums[i-1], dp[i-1][j])
        # print([i[0] for i in dp])
        # print([i[1] for i in dp])
        # print([i[2] for i in dp])
        return dp[n][0]
