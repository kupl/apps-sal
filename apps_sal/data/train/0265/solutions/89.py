class Solution:

    def maxNonOverlapping(self, nums, target):
        d = {0: -1}
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            found = prefix - target
            if found in d:
                count += 1
                d = {}
            d[prefix] = i
        return count
