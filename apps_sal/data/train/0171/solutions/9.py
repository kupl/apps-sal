class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        else:
            result = big = small = nums[0]
        for i in nums[1:]:
            big, small = max(i, i * big, i * small), min(i, i * small, i * big)
            result = max(result, big)
        return result
