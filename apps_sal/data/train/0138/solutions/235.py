class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return 0 if nums[0] < 0 else 1
        start = 0
        end = 0
        longest = 0
        while end < size:
            numNeg = 0
            leftNeg = -1
            rightNeg = -1
            while end < size and (not nums[end] == 0):
                if nums[end] < 0:
                    numNeg += 1
                    rightNeg = end
                    if leftNeg == -1:
                        leftNeg = end
                end += 1
            if numNeg % 2 == 0:
                longest = max(longest, end - start)
            else:
                longest = max(longest, end - rightNeg - 1, rightNeg - start, end - leftNeg - 1, leftNeg - start)
            end += 1
            start = end
        return longest
