class Solution:

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = y = float('inf')
        for n in nums:
            if n <= x:
                x = n
            elif n <= y:
                y = n
            else:
                return True
        return False
