class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left_idx = 0
        right_idx = len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while left_idx <= right_idx:
            if nums[left_idx] + nums[right_idx] > target:
                right_idx -= 1
            else:
                res += 1 << (right_idx - left_idx)
                res %= mod
                left_idx += 1
        return res
