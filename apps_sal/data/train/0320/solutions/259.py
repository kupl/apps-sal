class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for i in range(len(nums)):
                if nums[i] % 2:
                    count += 1
                    nums[i] -= 1
                nums[i] //= 2
            if not sum(nums):
                return count
            count += 1
        return count - 1
