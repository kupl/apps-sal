class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        one = 0
        for num in nums:
            (one, zero) = ((one ^ num & zero) & ~(~zero & one & num), (zero ^ num) & ~(~zero & one & num))
        return zero
