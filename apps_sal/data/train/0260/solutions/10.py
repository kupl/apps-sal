class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]]
        print(nums)
        total = min(2, len(nums))
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                total += 1
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                total += 1
        return total
