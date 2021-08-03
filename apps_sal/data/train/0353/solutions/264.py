class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if nums is None and len(nums) == 0:
            return 0

        nums.sort()
        mod = 10**9 + 7
        ans = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right - left, mod)
                left += 1

        return ans % mod
