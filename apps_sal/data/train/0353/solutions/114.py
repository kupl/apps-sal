class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        left, right = 0, len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right - left)
                left += 1
        return res % mod
