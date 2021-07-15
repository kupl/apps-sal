from typing import List, Tuple
class Solution:
    def maxNonOverlappingIntervals(self, intervals: List[Tuple[int, int]], sort=True) -> int:
        if not intervals:
            return 0
        # Sort intervals by ending time
        if sort:
            intervals = sorted(intervals, key=lambda x: x[1])
        ans = 1
        cur_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start <= cur_end:
                continue
            ans += 1
            cur_end = end
        return ans
        
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # If we can get all subarrays that sum to target in order sorted by ending index,
        # then we can simply apply activity selection to it.
        # We can use prefix sums to get this^^. Note that because negative numbers are allowed,
        # we might get multiple subarrays ending at i that sum to target. However, we can ignore
        # all except the smallest one, as we want non-overlapping.
        prefix_sum = {0: -1}
        cumsum = 0
        intervals = []
        for i, x in enumerate(nums):
            cumsum += x
            if cumsum - target in prefix_sum:
                intervals.append((prefix_sum[cumsum-target]+1, i))
            prefix_sum[cumsum] = i  # Don't bother with multiple indices, just use the the latest one
        return self.maxNonOverlappingIntervals(intervals, False)
