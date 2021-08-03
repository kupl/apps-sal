class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # track min_negative_product and max_positive_product

        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return nums[0]

        curr_min = curr_max = best_max = nums[0]

        for i in range(1, len(nums)):
            curr_min, curr_max = min(nums[i], nums[i] * curr_min, nums[i] * curr_max), max(nums[i], nums[i] * curr_min, nums[i] * curr_max)

            best_max = max(curr_max, best_max)

        return best_max
