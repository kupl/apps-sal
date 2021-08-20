class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10 ** 9 + 7
        (left, right) = (0, len(nums) - 1)
        for left in range(len(nums)):
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            if left <= right and nums[left] + nums[right] <= target:
                print((nums[left], nums[right]))
                res += pow(2, right - left, mod)
                res %= mod
        return res
