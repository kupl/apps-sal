
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nr = len(nums)
        dp = [[0] * 3 for _ in range(nr)]
        dp[0][nums[0] % 3] = nums[0]

        for i in range(1, nr):
            for j in range(3):
                dp[i][j] = dp[i - 1][j]

            for j in range(3):
                new_num = dp[i - 1][j] + nums[i]
                new_rem = new_num % 3

                if dp[i][new_rem] < new_num:
                    dp[i][new_rem] = new_num

        return dp[nr - 1][0]
