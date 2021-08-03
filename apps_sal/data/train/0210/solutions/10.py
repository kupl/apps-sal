class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        d = {}
        w = t + 1

        for i in range(len(nums)):
            b = nums[i] // w
            if b in d:
                return True
            if b - 1 in d and abs(nums[i] - d[b - 1]) < w:
                return True
            if b + 1 in d and abs(nums[i] - d[b + 1]) < w:
                return True
            d[b] = nums[i]
            if i >= k:
                del d[nums[i - k] // w]

        return False
