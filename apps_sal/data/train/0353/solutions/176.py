class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        n = len(nums)
        r = n - 1
        mod = 10**9 + 7
        c = 0

        while(l <= r):
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                c = (c + ((2**(r - l)) % mod)) % mod
                l += 1
        return c
