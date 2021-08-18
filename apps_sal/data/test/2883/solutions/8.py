
class Solution:
    def merge(self, intervals):
        si = sorted(intervals, key=lambda x: (x.start, x.end))
        cur = 1
        while cur < len(si):
            if si[cur - 1].end >= si[cur].start:
                si[cur - 1] = Interval(si[cur - 1].start, max(si[cur - 1].end, si[cur].end))
                del si[cur]
            else:
                cur += 1
        return si
