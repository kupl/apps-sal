class Solution:

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        while True:
            allzero = True
            for (index, num) in enumerate(nums):
                if num != 0:
                    allzero = False
                if num % 2 == 1:
                    nums[index] = num - 1
                    result += 1
            if allzero:
                break
            allzero = True
            for (index, num) in enumerate(nums):
                if num != 0:
                    allzero = False
                nums[index] = num // 2
            if allzero:
                break
            else:
                result += 1
        return result
