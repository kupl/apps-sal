class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        start = -1
        i = 0
        firstn = -1
        maxl = 0
        nneg = 0
        while i < len(nums):
            if nums[i] < 0:
                nneg += 1
                if firstn < 0:
                    firstn = i
                lastn = i
            elif nums[i] == 0:
                if nneg % 2 == 0:
                    maxl = max(maxl, i - start - 1)
                else:
                    maxl = max([maxl, lastn - start - 1, i - firstn - 1])
                start = i
                nneg = 0
                firstn = -1
            i += 1
        return maxl
