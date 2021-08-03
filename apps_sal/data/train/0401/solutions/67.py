class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        #         total_sum = sum(nums)
        #         sorted_nums = sorted(nums)
        #         print(sorted_nums)

        #         if total_sum%3 == 0:
        #             return total_sum
        #         curr_max = 0
        #         for i in range(length(sorted_nums)):
        #             if (total_sum - sorted_nums[i]) %3 == 0:
        #                 curr_max = (total_sum - sorted_nums[i])

        #             if (total_sum - sorted_nums[i]) %3 == 0:
        #                 curr_max = (total_sum - sorted_nums[i])

        dp = [0, float('-inf'), float('-inf')]
        for n in nums:
            dp = [max(dp[i], dp[(3 - n % 3 + i) % 3] + n) for i in range(3)]
        return dp[0]
