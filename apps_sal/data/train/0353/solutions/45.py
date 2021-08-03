class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        if nums[0] * 2 > target:
            return 0

        MOD = 10 ** 9 + 7
        count = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] + nums[right] > target:
                right -= 1
            if right < left:
                break
            count = (count + (1 << (right - left))) % MOD
            left += 1
        return count
