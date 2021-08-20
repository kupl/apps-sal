class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        mod = 10 ** 9 + 7
        nums.sort()
        (left, right) = (0, len(nums) - 1)
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += pow(2, right - left, mod)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)
