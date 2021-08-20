class Solution:

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        start = 0
        end = 0
        foundl = foundr = -1
        for (i, n) in enumerate(intervals):
            if foundl == -1 and newInterval.start <= n.end:
                foundl = 1
                start = i
                break
            else:
                continue
        for (i, n) in enumerate(intervals[::-1]):
            if foundr == -1 and newInterval.end >= n.start:
                foundr = 1
                end = len(intervals) - 1 - i
                break
            else:
                continue
        print(start, end, foundl, foundr)
        if foundl == 1 and foundr == 1:
            if start <= end:
                s = min(intervals[start].start, newInterval.start)
                e = max(intervals[end].end, newInterval.end)
                return intervals[:start] + [Interval(s, e)] + intervals[end + 1:]
            else:
                return intervals[:start] + [newInterval] + intervals[end + 1:]
        elif foundl == 1:
            return [newInterval] + intervals
        else:
            return intervals + [newInterval]
