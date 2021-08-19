class Solution:

    def minOperations(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        count = 0
        while nums != arr:
            f = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
                    f = 1
            if f == 0:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                count += 1
        return count
