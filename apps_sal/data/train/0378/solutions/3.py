class Solution:
    def search(self, nums, pos, target, seen):
        if (pos, target) in seen:
            return False
        if target == 0:
            return True
        if pos >= len(nums) or nums[pos] > target:
            return False
        if self.search(nums, pos + 1, target - nums[pos], seen):
            return True
        if self.search(nums, pos + 1, target, seen):
            return True
        seen.add((pos, target))
        return False

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        nums = sorted(nums)
        return self.search(nums, 0, target, set())
