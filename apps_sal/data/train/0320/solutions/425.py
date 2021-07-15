class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for i in range(len(nums)):
                if nums[i] == 1:
                    nums[i] = 0
                    count += 1
            if max(nums) < 1:
                break
            for i in range(len(nums)):
                if nums[i] < 2:
                    continue
                if nums[i] % 2 != 0:
                    count += 1
                nums[i] //= 2
            count += 1
        return count
