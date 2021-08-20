class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        import sortedcontainers
        sl = sortedcontainers.SortedList()
        (start, end) = (0, 0)
        best = 0
        while end < len(nums):
            sl.add(nums[end])
            if sl[-1] - sl[0] <= limit:
                best = max(best, len(sl))
            else:
                while sl[-1] - sl[0] > limit:
                    sl.remove(nums[start])
                    start += 1
            end += 1
        return best
