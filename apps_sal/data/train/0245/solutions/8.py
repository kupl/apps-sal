class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        result = ""

        numsCount = len(nums)

        for i in range(numsCount):
            thisNum = nums[i]

            strNum = str(thisNum)

            if i == 0:
                result = result + strNum
            elif i == 1 and numsCount > 2:
                result = result + "/(" + strNum
            elif i == numsCount - 1 and numsCount > 2:
                result = result + "/" + strNum + ")"
            else:
                result = result + "/" + strNum

        return result
