class Solution:

    def minOperations(self, nums: List[int]) -> int:
        zeroIndexes = set()
        result = 0
        isEven = False
        while len(zeroIndexes) != len(nums):
            if isEven:
                for i in range(len(nums)):
                    nums[i] >>= 1
                result += 1
                isEven = False
            else:
                for i in range(len(nums)):
                    if i not in zeroIndexes:
                        if nums[i] & 1:
                            nums[i] -= 1
                            result += 1
                        if nums[i] == 0:
                            zeroIndexes.add(i)
                isEven = True
        return result
