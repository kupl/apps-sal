class Solution:
    def minOperations(self, nums: List[int]) -> int:

        cnt = 0

        while nums.count(0) < len(nums):
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    cnt += 1

            if nums.count(0) != len(nums):
                for i in range(len(nums)):
                    nums[i] = nums[i] / 2
                cnt += 1
            else:
                return cnt
