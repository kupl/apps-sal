class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        ans = 0
        m = 10 ** 9 + 7
        nums.sort()
        while l <= r:
            if (nums[l] + nums[r] > target):
                r -= 1
            else:
                ans += pow(2, r - l, m)
                l += 1
        return ans % m
