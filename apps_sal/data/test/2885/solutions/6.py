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
         start, end = newInterval.start, newInterval.end
         left, right = [], []
         for i in intervals:
             if i.end < start:
                 left.append(i)
             elif i.start > end:
                 right.append(i)
             else:
                 start = min(start, i.start)
                 end = max(end,i.end)
         return left + [Interval(start, end)] + right
