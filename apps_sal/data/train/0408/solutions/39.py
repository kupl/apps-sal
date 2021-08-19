class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        nums = [-x for x in arr]
        heapify(nums)
        currSum = sum(arr)
        N = len(nums)
        bestVal = -nums[0]
        bestDifference = float('inf')

        def testValue(value):
            sumWithIdeal = currSum + numElementsToChange * value
            difference = abs(target - sumWithIdeal)
            if value <= nextLargest and value >= (-nums[0] if nums else 0):
                if difference < bestDifference:
                    return (int(value), abs(target - sumWithIdeal))
                elif difference == bestDifference:
                    return (min(bestVal, int(value)), bestDifference)
            return (bestVal, bestDifference)
        while nums:
            nextLargest = -heappop(nums)
            currSum -= nextLargest
            numElementsToChange = N - len(nums)
            if currSum <= target:
                idealValue = (target - currSum) / numElementsToChange
                if idealValue.is_integer():
                    (bestVal, bestDifference) = testValue(idealValue)
                else:
                    (bestVal, bestDifference) = testValue(floor(idealValue))
                    (bestVal, bestDifference) = testValue(ceil(idealValue))
        return bestVal
