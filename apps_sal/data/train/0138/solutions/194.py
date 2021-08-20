class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        positive_index = -1
        negative_index = -1
        sums = 1
        result = 0
        for i in range(len(nums)):
            if sums * nums[i] < 0:
                sums = -1
            elif sums * nums[i] > 0:
                sums = 1
            if nums[i] == 0:
                positive_index = i
                negative_index = -1
                sums = 1
            elif sums > 0:
                result = max(result, i - positive_index)
            elif negative_index == -1:
                negative_index = i
            else:
                result = max(result, i - negative_index)
                print(result)
        return result
