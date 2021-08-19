class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        withAdding = [0 for _ in range(len(nums))]
        notAdding = [-1 for _ in range(len(nums))]
        validMax = [nums[0]]
        maxValue = nums[0]
        withAdding[0] = nums[0]
        for i in range(1, len(nums)):
            if maxValue < 0 and nums[i] > maxValue:
                withAdding[i] = nums[i]
            else:
                withAdding[i] = maxValue + nums[i]
            validMax.append(withAdding[i])
            maxValue = max(withAdding[i], maxValue)
            if len(validMax) > k and validMax.pop(0) == maxValue:
                maxValue = max(validMax)
            notAdding[i] = max(notAdding[i - 1], withAdding[i - 1])
        return max(max(notAdding), max(withAdding))
