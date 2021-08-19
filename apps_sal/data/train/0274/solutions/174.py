class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()
        l = r = 0
        result = 1
        for r in range(len(nums)):
            sl.add(nums[r])
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[l])
                l += 1
            result = max(len(sl), result)
        return result
