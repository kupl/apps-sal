class Solution:
    def partition(self, nums, target, current, pos, fill):
        if fill == 0:
            return True
        for i in range(pos, len(nums)):
            next = nums[:i] + nums[i + 1:]
            if current + nums[i] == target:
                if self.partition(next, target, 0, 0, fill - 1):
                    return True
            elif current + nums[i] < target:
                if self.partition(next, target, current + nums[i], i, fill):
                    return True
            elif current == 0:
                return False
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        if s % k > 0:
            return False
        target = s // k

        return self.partition(nums, target, 0, 0, k)
