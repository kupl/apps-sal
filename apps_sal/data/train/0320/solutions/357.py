class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums or sum(nums) == 0: return 0
        cnt = 0
        while sum(nums) != 0:
            if all(num % 2 == 0 for num in nums):
                cnt += 1
                for i in range(len(nums)):
                    nums[i] //= 2
            else:
                for i in range(len(nums)):
                    if nums[i] % 2:
                        cnt += 1
                        nums[i] -= 1
        return cnt
