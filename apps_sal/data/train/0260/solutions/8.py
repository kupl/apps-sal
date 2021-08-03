class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) < 2:
            return 1
        max_length = 1
        state = 0
        i = 1
        while i < len(nums):
            while state == 0 and i < len(nums):
                if nums[i - 1] > nums[i]:
                    max_length = max_length + 1
                    state = 2
                if nums[i - 1] < nums[i]:
                    max_length = max_length + 1
                    state = 1
                i = i + 1
            while state == 1 and i < len(nums):
                if nums[i - 1] > nums[i]:
                    max_length = max_length + 1
                    state = 2
                i = i + 1
            while state == 2 and i < len(nums):
                if nums[i - 1] < nums[i]:
                    state = 1
                    max_length = max_length + 1
                i = i + 1
        return max_length
