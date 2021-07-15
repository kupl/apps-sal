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
         left = [i for i in intervals if start > i.end]
         right = [i for i in intervals if end < i.start]
         if left + right != intervals:
             start = min(start, intervals[len(left)].start)
             end = max(end, intervals[~len(right)].end)
         return left + [Interval(start, end)] + right
             
                 
             
