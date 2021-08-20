class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxNum = nums[0]
        maxSum = nums[0]
        maxNegSum = 0
        curNegWindowSum = 0
        curWindowSum = 0
        rightIndex = 0
        leftIndex = 0
        midIndex = 0
        negativeStreak = False
        while rightIndex < len(nums):
            if maxNum < nums[rightIndex]:
                maxNum = nums[rightIndex]
            if nums[rightIndex] >= 0 and (not negativeStreak):
                curWindowSum += nums[rightIndex]
                maxSum = max(maxSum, curWindowSum)
            elif nums[rightIndex] < 0 and (not negativeStreak):
                negativeStreak = True
                midIndex = rightIndex
                if k > 1:
                    curNegWindowSum = nums[rightIndex]
                    maxNegSum = curNegWindowSum
                curWindowSum += nums[rightIndex]
            elif nums[rightIndex] < 0 and negativeStreak:
                if rightIndex - midIndex < k - 1:
                    curNegWindowSum += nums[rightIndex]
                    maxNegSum = curNegWindowSum
                else:
                    if k > 1:
                        curNegWindowSum -= nums[midIndex]
                        curNegWindowSum += nums[rightIndex]
                    maxNegSum = min(maxNegSum, curNegWindowSum)
                    midIndex += 1
                curWindowSum += nums[rightIndex]
            elif nums[rightIndex] >= 0 and negativeStreak:
                curWindowSum -= maxNegSum
                if curWindowSum <= 0:
                    midIndex = rightIndex
                    leftIndex = rightIndex
                    curWindowSum = nums[rightIndex]
                else:
                    curWindowSum += nums[rightIndex]
                maxSum = max(maxSum, curWindowSum)
                maxNegSum = 0
                curNegWindowSum = 0
                negativeStreak = False
            rightIndex += 1
        return max(maxSum, maxNum)
