class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums) - 1
        left = 0
        ret = 0
        while left < right:
            max_right = target - nums[left]
            while left < right and max_right < nums[right]:
                right -= 1
            if left < right:
                ret += 2 ** (right - left) - 1
            left += 1
        for i in range(len(nums)):
            if nums[i] * 2 > target:
                break
            ret += 1
        return ret % 1000000007
