class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        maxLen = 0
        tovisit = set([i for i in range(len(nums))])
        while len(tovisit) > 0:
            p = tovisit.pop()
            curr = 1
            while nums[p] != -1 and nums[p] in tovisit:
                tovisit.remove(nums[p])
                nums[p], p = -1, nums[p]
                curr += 1
            maxLen = max(maxLen, curr)
        return maxLen
