# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        for interval in intervals:
            if newInterval and newInterval.end >= interval.start and newInterval.start <= interval.end:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
            else:
                if newInterval and newInterval.end < interval.start:
                    result.append(newInterval)
                    result.append(interval)
                    newInterval = None
                else:
                    result.append(interval)
        if newInterval:
            result.append(newInterval)
        return result