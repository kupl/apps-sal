class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        mod = int(1e9 + 7)
        power = [1] * (len(nums) + 1)
        for i in range(1, len(nums)):
            power[i] = power[i - 1] * 2 % mod

        left, right = 0, len(nums) - 1
        res = 0
        while left <= right:
            while left <= right and nums[left] + nums[right] > target:
                right -= 1

            if left > right:
                break
            res += power[right - left]
            left += 1

        return res % mod
