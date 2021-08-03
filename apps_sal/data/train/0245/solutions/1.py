class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s = '/'.join(map(str, nums))
        if len(nums) <= 2:
            return s
        s = s.replace('/', '/(', 1) + ')'
        return s
