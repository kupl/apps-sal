class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums) - 1
        left = 0
        ret = 0
        while left < right:
            if nums[left] * 2 <= target:
                ret += 1
            max_right = target - nums[left]
            while left < right and max_right < nums[right]:
                if nums[right] * 2 <= target:
                    ret += 1
                right -= 1
            if left < right:
                ret += 2 ** (right - left) - 1
            else:
                return ret % 1000000007
            left += 1
        if nums[right] * 2 <= target:
            ret += 1
        return ret % 1000000007
