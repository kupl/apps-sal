class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while (left <= right):
            if nums[left] + nums[right] <= target:
                res += pow(2, (right - left), mod)
                left += 1
            else:
                right -= 1
        return res % mod
