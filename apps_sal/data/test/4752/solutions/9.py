class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        while start < end:
            curr_sum = sorted_nums[start] + sorted_nums[end]
            if (curr_sum == target):
                break
            if (curr_sum < target):
                start += 1
            else:
                end -= 1
        first_index = nums.index(sorted_nums[start])
        second_index = nums.index(sorted_nums[end])
        if sorted_nums[start] == sorted_nums[end]:
            nums.pop(first_index)
            second_index = nums.index(sorted_nums[end]) + 1
        return [first_index, second_index]
