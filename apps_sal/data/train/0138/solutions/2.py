class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l = len(nums)
        start = 0
        subArrays = []
        for i in range(l):
            if nums[i] == 0:
                subArrays.append(self.findOptimal(nums[start:i]))
                start = i + 1
                end = i + 1

        subArrays.append(self.findOptimal(nums[start:l]))

        return max(subArrays)

    def findOptimal(self, nums: List[int]) -> int:
        if not nums:
            return 0

        negs = 0
        l = 0
        for i in nums:
            l += 1
            if i < 0:
                negs += 1

        if negs % 2 == 0:
            return l
        else:
            i = 0
            j = l - 1
            while i < j:
                if nums[i] < 0 or nums[j] < 0:
                    return l - 1
                i += 1
                j -= 1
                l -= 1

        return 0
