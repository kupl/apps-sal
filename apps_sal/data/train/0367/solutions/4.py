class Solution:

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return list(filter(lambda x: x[1] > 1, c.items()))[0][0]
