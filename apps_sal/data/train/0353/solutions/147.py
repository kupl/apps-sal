class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l = 0
        r = len(nums) - 1
        mod = 10 ** 9 + 7
        while l <= r:                       ##min和max值可以相等！！
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 2 ** (r - l) % mod
                l += 1                  ##这个开头的最大值！！
        return res % mod
        

