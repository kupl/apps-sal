class Solution:

    def search_interval(self, start, end, nums, target):
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        size = end - start
        half = size // 2
        new_start_1 = start
        new_end_1 = start + half
        new_start_2 = start + half + 1
        new_end_2 = end
        first_half_sorted = False
        first_half_contains = False
        second_half_sorted = False
        second_half_contains = False
        if nums[new_end_1] >= nums[new_start_1]:
            first_half_sorted = True
            if target >= nums[new_start_1] and target <= nums[new_end_1]:
                first_half_contains = True
        if nums[new_end_2] >= nums[new_start_2]:
            second_half_sorted = True
            if target >= nums[new_start_2] and target <= nums[new_end_2]:
                second_half_contains = True
        if first_half_contains:
            return self.search_interval(new_start_1, new_end_1, nums, target)
        elif second_half_contains:
            return self.search_interval(new_start_2, new_end_2, nums, target)
        elif first_half_sorted:
            return self.search_interval(new_start_2, new_end_2, nums, target)
        elif second_half_sorted:
            return self.search_interval(new_start_1, new_end_1, nums, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        return self.search_interval(0, len(nums) - 1, nums, target)
