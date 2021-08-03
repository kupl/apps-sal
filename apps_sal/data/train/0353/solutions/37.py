class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        sum, l, r = 0, 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                sum += (1 << r - l) % mod
                l += 1
        return sum % mod
