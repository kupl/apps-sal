
import operator


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        returnedList = []
        if(len(intervals) == 0):
            returnedList.append(newInterval)
            return returnedList

        p = 1
        for i in range(len(intervals)):
            if(intervals[i].end < newInterval.start):
                returnedList.append(intervals[i])
            elif(intervals[i].end == newInterval.start):
                newInterval.start = intervals[i].start
            elif(newInterval.start < intervals[i].end and newInterval.end > intervals[i].start):
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            elif(newInterval.end == intervals[i].start):
                newInterval.end = intervals[i].end
            elif(newInterval.end < intervals[i].start):
                p = 0
                break

        returnedList.append(newInterval)
        if(p == 0):
            returnedList.extend(intervals[i:])
        return returnedList
