class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        subsequences = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                subsequences += 1 << (r - l)
                l += 1
            else:
                subsequences += 1 if 2 * nums[r] <= target else 0
                r -= 1
            subsequences %= 1000000007
        return subsequences
