class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        MOD = 10**9 + 7
        p = 0
        while p < len(nums):
            while p < len(nums) and nums[p] + nums[-1] > target:
                nums.pop()
            if len(nums)-p-1 >= 0:
                res += pow(2, len(nums)-p-1, MOD)
            p += 1
        return res%MOD

