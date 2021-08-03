class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return(False)
        min = nums[0]
        sec_min = (2**31 - 1)

        for i in nums:
            if i <= min:
                min = i
            else:
                if i <= sec_min:
                    sec_min = i
                else:
                    return(True)
        return(False)
