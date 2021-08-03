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
        length = len(intervals)
        if length == 1 or length == 0:
            return intervals
        intervals.sort(key=lambda l: l.start)
        result = []
        curr = intervals.pop(0)
        while intervals:
            next_int = intervals.pop(0)
            if curr.end >= next_int.start:
                curr.end = max(next_int.end, curr.end)
            else:
                result.append(curr)
                curr = next_int
        result.append(curr)
        return result
