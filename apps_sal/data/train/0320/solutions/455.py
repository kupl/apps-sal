class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i = 0
        k = 0
        for x in range(10**9):
            if nums == [0.0] * len(nums):
                break
            if i >= 1:
                k+=1
                i = 0
            for y in range(len(nums)):
                if nums[y] % 2 != 0:
                    nums[y] -= 1
                    k+=1
                if nums[y] % 2 == 0:
                    nums[y] = nums[y] / 2
                    i+=1
        return k
