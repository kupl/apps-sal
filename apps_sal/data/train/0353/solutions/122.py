class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (l, r) = (0, len(nums) - 1)
        re = 0
        while l <= r:
            while r >= l and nums[l] + nums[r] > target:
                r -= 1
            if r < l:
                break
            re += 2 ** (r - l)
            l += 1
        return re % 1000000007
