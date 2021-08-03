class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = (10**9) + 7
        right = len(nums) - 1
        res = 0
        left = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += 2**(right - left)
                res = res % mod
                left += 1

        return res
