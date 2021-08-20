class Solution:

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        diffs = []
        for i in range(1, len(nums)):
            diffs.append(nums[i] - nums[i - 1])
        prev_idx = 0
        while diffs[prev_idx] == 0:
            prev_idx += 1
            if prev_idx == len(diffs):
                return 1
        cnt = 2
        for i in range(prev_idx + 1, len(diffs)):
            if diffs[prev_idx] * diffs[i] < 0:
                cnt += 1
                prev_idx = i
        return cnt
