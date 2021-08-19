class Solution:

    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        while sum(nums) != 0:
            all_even = True
            for i in range(N):
                if nums[i] & 1:
                    all_even = False
                    res += 1
                    nums[i] -= 1
            if all_even:
                res += 1
                nums = [n // 2 for n in nums]
        return res
