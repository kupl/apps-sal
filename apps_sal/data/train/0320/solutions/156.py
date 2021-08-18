class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
            all_zero = True
            for i in range(len(nums)):
                if nums[i] != 0:
                    all_zero = False
                nums[i] //= 2
            if all_zero:
                return count
            count += 1
        return count
