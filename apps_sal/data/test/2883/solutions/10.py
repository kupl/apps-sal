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
         length=len(intervals)
         if length==1 or length==0: return intervals
         intervals.sort(key=lambda l:l.start)
         index=0
         while index<len(intervals)-1:
             curr=intervals[index]
             if curr.end>=intervals[index+1].start:
                 intervals.pop(index)
                 next_int=intervals.pop(index)
                 if curr.end<next_int.end:
                     curr.end=next_int.end
                 intervals.insert(index,curr)
             else:
                 index+=1
         return intervals
     
