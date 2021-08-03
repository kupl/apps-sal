class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_count = 0
        start = 0
        zero = 2

        for i in range(len(nums)):
            if nums[i] == 0:
                zero -= 1
            while zero < 1:
                if nums[start] == 0:
                    zero += 1
                start += 1
            max_count = max(max_count, i - start)

        return max_count
