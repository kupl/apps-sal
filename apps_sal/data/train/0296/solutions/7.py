class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if nums[len(nums) - 1] > nums[0]:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == nums[start]:
                start += 1
            elif nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])
