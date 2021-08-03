class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        tails = [-float('inf')] + [float('inf')] * 3
        for x in nums:
            for i in range(2, -1, -1):
                if x > tails[i]:
                    tails[i + 1] = x
                    break
            if tails[-1] < float('inf'):
                return True
        return False
