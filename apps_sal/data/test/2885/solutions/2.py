# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import operator
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        #Leetcode 第56题的思路
        returnedList = []
        if(len(intervals) == 0):
            returnedList.append(newInterval)
            return returnedList

        p = 1       #判断是循环结束跳出循环，还是newInterval.end < intervals[i].start跳出循环，前者不进行拼接
        for i in range(len(intervals)):
            if(intervals[i].end < newInterval.start):
                returnedList.append(intervals[i])
            elif(intervals[i].end == newInterval.start):
                newInterval.start = intervals[i].start
            elif(newInterval.start < intervals[i].end and newInterval.end > intervals[i].start): #相交
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