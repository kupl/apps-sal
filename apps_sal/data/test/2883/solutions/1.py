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
         if len(intervals) < 2:
             return intervals
         intervals = sorted(intervals, key=lambda s: s.start)
         rs = []
         cur = intervals[0]
         for r in intervals[1:]:
             if r.start <= cur.end:
                 cur.end = max(r.end, cur.end)
             else:
                 rs.append(cur)
                 cur = r
         rs.append(cur)
         return rs
         
