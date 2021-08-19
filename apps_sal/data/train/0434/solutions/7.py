class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        (start, end, maxlen, k) = (0, 0, 0, 1)
        while end < len(nums):
            if nums[end] == 0:
                k = k - 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start = start + 1
                end = end + 1
                continue
            if k >= 0 or nums[end] == 1:
                maxlen = max(maxlen, end - start)
                end = end + 1
        return maxlen
