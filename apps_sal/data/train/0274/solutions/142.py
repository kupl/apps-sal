from sortedcontainers import SortedList


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        start = 0
        ans = 0
        for end in range(len(nums)):
            x = nums[end]
            sl.add(x)
            while sl[-1] - sl[0] > limit and start <= end:
                sl.remove(nums[start])
                start += 1
            if start <= end:
                ans = max(ans, end - start + 1)
        return ans
