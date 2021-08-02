# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        si = sorted(intervals, key=lambda x: (x.start, x.end))
        cur = 1  # index of current tuple
        while cur < len(si):
            # check intersection of current and previous tuple
            # if end of previous is less than begin of current
            # there are the intersection, we should merge them
            # into the bigger interval
            if si[cur - 1].end >= si[cur].start:
                # change end of the interval(tuple)
                si[cur - 1] = Interval(si[cur - 1].start, max(si[cur - 1].end, si[cur].end))
                # delete unnecessary interval(tuple)
                del si[cur]
            # there are no intersection, go to the next tuple
            else:
                cur += 1
        return si
        