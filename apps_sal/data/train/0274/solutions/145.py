class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        maxStack = []

        minStack = []
        result = 1

        leftPos = 0
        for i in range(0, len(nums)):
            while maxStack and nums[i] < nums[maxStack[0]] - limit:
                leftPos = max(leftPos, maxStack.pop(0) + 1)

            while minStack and nums[i] > nums[minStack[0]] + limit:
                leftPos = max(leftPos, minStack.pop(0) + 1)

            length = i - leftPos + 1
            if length > result:
                result = length

            while maxStack and nums[i] > nums[maxStack[-1]]:
                maxStack.pop()
            maxStack.append(i)
            while minStack and nums[i] < nums[minStack[-1]]:
                minStack.pop()
            minStack.append(i)

        return result
