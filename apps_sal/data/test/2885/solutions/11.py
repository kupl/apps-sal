
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x.start)

        i = 0
        while i < len(intervals) - 1:
            left = intervals[i]
            right = intervals[i + 1]
            if left.end >= right.start:
                intervals[i] = Interval(s=left.start, e=max(left.end, right.end))
                del intervals[i + 1]
            else:
                i += 1

        return intervals
