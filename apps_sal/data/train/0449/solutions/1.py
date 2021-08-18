class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        if nums[-1] > nums[0]:
            return nums[0]

        boundary = nums[0]
        return self.binary_search_min(nums, boundary)

    def binary_search_min(self, nums, maximum):
        """
        Binary search for the minimum element, assuming that every element >= maximum indicates leaving the array to the left
        """
        left_boundary = 0
        right_boundary = len(nums) - 1

        while True:
            current_index = left_boundary + (right_boundary - left_boundary) // 2
            value = nums[current_index]

            if left_boundary == right_boundary:
                return value

            if value >= maximum:
                left_boundary = current_index + 1
            else:
                right_boundary = current_index
