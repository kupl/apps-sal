class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (lo, hi, ans) = (0, len(nums) - 1, 0)
        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
                continue
            ans += 2 ** (hi - lo)
            lo += 1
        return ans % (10 ** 9 + 7)
