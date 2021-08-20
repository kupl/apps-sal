class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_length = 0
        count = 0
        for (idx, v) in enumerate(nums):
            if count == 0:
                count += 1
                max_length = max(max_length, count)
            if idx + 1 < len(nums):
                n_v = nums[idx + 1]
                if n_v == v + 1:
                    count = count + 1
                elif n_v == v:
                    continue
                else:
                    max_length = max(max_length, count)
                    count = 0
        max_length = max(max_length, count)
        return max_length
