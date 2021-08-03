class Solution:
    def insert(self, intervals, newInterval):
        start = len(intervals)
        for i in range(len(intervals)):
            if newInterval.start < intervals[i].start:
                start = min(start, i)
            if not (newInterval.start > intervals[i].end or newInterval.end < intervals[i].start):
                newInterval = Interval(min(newInterval.start, intervals[i].start), max(newInterval.end, intervals[i].end))
                start, intervals[i] = min(i, start), []
        intervals = [ele for ele in intervals if ele != []]
        intervals.insert(start, newInterval)
        return intervals
