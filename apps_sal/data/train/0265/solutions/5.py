class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        curSum = 0
        sumsSet = {0}
        result = 0
        for x in nums:
            curSum += x
            if (curSum - target) in sumsSet:
                result += 1
                curSum = 0
                sumsSet.clear()
            sumsSet.add(curSum)

        return result
