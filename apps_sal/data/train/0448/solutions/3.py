class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False

        if k == 1:
            return True

        cur_sum, sums = 0, {0: -1}
        for i, x in enumerate(nums):
            cur_sum += x
            mod = (cur_sum % k) if k != 0 else cur_sum
            if mod in sums:
                if i - sums[mod] >= 2:
                    return True
            else:
                sums[mod] = i
        return False
