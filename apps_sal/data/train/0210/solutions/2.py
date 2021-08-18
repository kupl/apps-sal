class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        import sys

        bh = {}
        w = t + 1
        for i in range(len(nums)):
            n_i = nums[i]
            n_i_w = n_i // w
            if n_i_w in bh:
                return True
            if n_i_w - 1 in bh and abs(n_i - bh[n_i_w - 1]) < w:
                return True
            if n_i_w + 1 in bh and abs(n_i - bh[n_i_w + 1]) < w:
                return True
            bh[n_i_w] = nums[i]
            if len(bh) > k:
                del bh[(nums[i - k]) // w]
        return False
