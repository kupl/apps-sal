import bisect


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if limit < 0:
            return 0

        n = len(nums)
        if n < 2:
            return n

        # sliding window to calculate min-max range
        # extend window if range is within limit r -->
        # shrink window if range is off limit l -->
        # sliding window is a sorted subarray

        longest = 1
        l, r = 0, 0
        window = []
        while l < n and r < n:
            if not window:
                window.append(nums[r])
                r += 1
            else:
                curr = nums[r]
                minimum, maximum = window[0], window[-1]
                if abs(curr - minimum) <= limit and abs(curr - maximum) <= limit:
                    bisect.insort(window, curr)
                    r += 1
                    longest = max(longest, r - l)
                else:
                    window.remove(nums[l])
                    l += 1
        return longest
