class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (l, r, count) = (0, len(nums) - 1, 0)
        mod = 10 ** 9 + 7
        while l <= r:
            sums = nums[l] + nums[r]
            if sums > target:
                r -= 1
            else:
                count += 2 ** (r - l)
                l += 1
        return count % mod
