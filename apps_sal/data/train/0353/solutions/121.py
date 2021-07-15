class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = 10 ** 9 + 7
        l = 0
        r = len(nums) - 1
        res = 0
        
        while l <= r:
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            if l <= r:
                res += 2 ** (r - l)
                l += 1
            else:
                break
        return res % m
