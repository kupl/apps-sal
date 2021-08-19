from sortedcontainers import SortedDict


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        startWindow = 0
        runningDict = SortedDict()
        maxWindow = 0
        for endWindow in range(len(nums)):
            if nums[endWindow] not in runningDict:
                runningDict[nums[endWindow]] = 0
            runningDict[nums[endWindow]] += 1
            (minKey, maxKey) = (runningDict.peekitem(0), runningDict.peekitem(-1))
            (minKey, maxKey) = (minKey[0], maxKey[0])
            while abs(maxKey - minKey) > limit and startWindow < endWindow:
                runningDict[nums[startWindow]] -= 1
                if runningDict[nums[startWindow]] == 0:
                    del runningDict[nums[startWindow]]
                (minKey, maxKey) = (runningDict.peekitem(0), runningDict.peekitem(-1))
                (minKey, maxKey) = (minKey[0], maxKey[0])
                startWindow += 1
            maxWindow = max(maxWindow, endWindow - startWindow + 1)
        return maxWindow
