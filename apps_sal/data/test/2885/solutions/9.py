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
         res = []
         for interval in intervals:
             if self.merge(interval, newInterval):
                 newInterval = Interval(min(interval.start, newInterval.start), max(interval.end, newInterval.end))
             else:
                 if newInterval != None and newInterval.end < interval.start:
                     res.append(newInterval)
                     newInterval = None
                 res.append(interval)
         if newInterval != None:
             res.append(newInterval)
         return res
     
     def merge(self, a, b):
         if b is None or a.start > b.end or a.end < b.start:
             return False
         return True
