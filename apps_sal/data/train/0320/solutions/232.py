class Solution:

    def getOdd(self, nums):
        for i, n in enumerate(nums):
            if n % 2 == 1:
                return i
        return None

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while nums.count(0) != len(nums):
            odd = self.getOdd(nums)
            if odd is None:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                res += 1
            else:
                for i in range(len(nums)):
                    if nums[i] % 2 == 1:
                        nums[i] = nums[i] - 1
                        res += 1

        return res
