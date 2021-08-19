class Solution:

    def check(self, nums, start, size):
        for i in range(start + 1, start + size + 1):
            if i >= len(nums) or nums[i] >> 6 != 2:
                return False
        return True

    def validUtf8(self, nums, start=0):
        """
        :type data: List[int]
        :rtype: bool
        """
        while start < len(nums):
            first = nums[start]
            if first >> 3 == 30 and self.check(nums, start, 3):
                start += 4
            elif first >> 4 == 14 and self.check(nums, start, 2):
                start += 3
            elif first >> 5 == 6 and self.check(nums, start, 1):
                start += 2
            elif first >> 7 == 0:
                start += 1
            else:
                return False
        return True
