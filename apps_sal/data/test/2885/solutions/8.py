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
        if not intervals:
            return [newInterval]
        v = []
        a = newInterval.start
        b = newInterval.end
        flag = 0
        s = a
        e = b
        for i in intervals:
            if i.start <= a <= i.end:
                s = i.start
            if i.start <= b <= i.end:
                e = i.end
                v.append(Interval(s, e))
                flag = 1
            if not flag and i.start > b:
                v.append(Interval(s, e))
                flag = 1
            if i.end < a or i.start > b:
                v.append(i)
        if not flag:
            v.append(Interval(s, e))
        return v
