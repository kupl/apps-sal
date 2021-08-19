class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # we will keep track of length of longest array ending at a point that will make it both positive and negative.
        # we will have input be index terminating.
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
        for i in range(1, numLength):  # can just use enumerate
            currentNum = nums[i]
            maxProducts[i] = [0, 0]  # need to default before initializing entries
            if currentNum > 0:
                maxProducts[i][0] = maxProducts[i - 1][0] + 1
                maxProducts[i][1] = maxProducts[i - 1][1] if maxProducts[i - 1][1] == 0 else maxProducts[i - 1][1] + 1
            elif currentNum < 0:
                maxProducts[i][1] = maxProducts[i - 1][0] + 1
                maxProducts[i][0] = maxProducts[i - 1][1] if maxProducts[i - 1][1] == 0 else maxProducts[i - 1][1] + 1  # need to be careful about 0 as those affect whether you can actually just add one or not.
            maxSize = max(maxSize, maxProducts[i][0])
        # print(maxProducts)

        return maxSize
