# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda a: (a.start, a.end))
        ptr = 0
        while ptr < len(intervals) - 1:
            if intervals[ptr].end >= intervals[ptr + 1].start:
                p = intervals.pop(ptr + 1)
                intervals[ptr].end = max(intervals[ptr].end, p.end)
            else:
                ptr += 1

        return intervals
