class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        count = 0
        while left <= right:
            t = nums[left] + nums[right]
            if t > target:
                right -= 1
            else:
                count += 2**(right - left)
                left += 1

        return count % mod
