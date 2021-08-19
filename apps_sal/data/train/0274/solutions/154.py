class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        n = len(nums)
        (l, r) = (0, -1)
        (max_window, min_window) = (deque(), deque())
        while r < n - 1:
            r += 1
            while max_window and max_window[-1] < nums[r]:
                max_window.pop()
            while min_window and min_window[-1] > nums[r]:
                min_window.pop()
            max_window.append(nums[r])
            min_window.append(nums[r])
            if max_window[0] - min_window[0] > limit:
                if max_window[0] == nums[l]:
                    max_window.popleft()
                if min_window[0] == nums[l]:
                    min_window.popleft()
                l += 1
        return r - l + 1
