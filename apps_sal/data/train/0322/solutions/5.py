class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        current_max = 1
        i = 0
        count = 0
        while current_max <= n:
            if i < len(nums) and nums[i] <= current_max:
                current_max += nums[i]
                i += 1
            else:
                current_max += current_max
                count += 1
        return count
