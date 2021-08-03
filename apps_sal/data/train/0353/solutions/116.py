class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        res = 0
        left, right = 0, N - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += 2 ** (right - left)
                left += 1
        return res % (10**9 + 7)
