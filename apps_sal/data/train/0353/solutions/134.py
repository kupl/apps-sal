class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        module = 10 ** 9 + 7
        ret = 0
        (lo, hi) = (0, n - 1)
        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                ret += 1 << hi - lo
                lo += 1
        return ret % module
