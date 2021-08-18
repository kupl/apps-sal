class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxProducts = {}
        numLength = len(nums)
        maxSize = 0
        if nums[0] == 0:
            maxProducts[0] = [0, 0]
        elif nums[0] > 0:
            maxProducts[0] = [1, 0]
        else:
            maxProducts[0] = [0, 1]
        maxSize = max(maxSize, maxProducts[0][0])
        for i in range(1, numLength):
            currentNum = nums[i]
            maxProducts[i] = [0, 0]
            if currentNum > 0:
                maxProducts[i][0] = maxProducts[i - 1][0] + 1
                maxProducts[i][1] = maxProducts[i - 1][1] if maxProducts[i - 1][1] == 0 else maxProducts[i - 1][1] + 1
            elif currentNum < 0:
                maxProducts[i][1] = maxProducts[i - 1][0] + 1
                maxProducts[i][0] = maxProducts[i - 1][1] if maxProducts[i - 1][1] == 0 else maxProducts[i - 1][1] + 1
            maxSize = max(maxSize, maxProducts[i][0])

        return maxSize
