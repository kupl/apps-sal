class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += 2 ** (right - left)
                left += 1
        return ans % mod
