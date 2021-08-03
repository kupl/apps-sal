class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        nums.sort()
        res = 0
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                res += pow(2, hi - lo)
                lo += 1

        return res % (pow(10, 9) + 7)
