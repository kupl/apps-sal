class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        cnt = 0
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                cnt += pow(2, hi - lo, MOD)
                lo += 1
        return cnt % MOD
