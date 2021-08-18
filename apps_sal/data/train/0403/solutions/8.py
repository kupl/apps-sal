class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        minN = nums[0]
        minSecond = None

        for i in range(1, len(nums)):
            if type(minSecond) == int and nums[i] > minSecond:
                return True

            if minN < nums[i]:
                if type(minSecond) == int and minSecond > nums[i]:
                    minSecond = nums[i]
                elif not type(minSecond) == int:
                    minSecond = nums[i]

            minN = min(minN, nums[i])

        return False
