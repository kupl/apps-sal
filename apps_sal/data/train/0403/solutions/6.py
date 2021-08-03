class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        a = b = None

        for i in nums:
            if a is None or a >= i:
                a = i
            elif b is None or b >= i:
                b = i
            else:
                return True

        return False
