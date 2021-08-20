class Solution:

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        inters = sorted(intervals, key=lambda intval: intval.start)
        ret = []
        n = len(intervals)
        if n == 0:
            return ret
        s = inters[0].start
        e = inters[0].end
        for i in range(1, n):
            if inters[i].start <= e:
                e = max(inters[i].end, e)
            else:
                ret.append(Interval(s, e))
                s = inters[i].start
                e = inters[i].end
        ret.append(Interval(s, e))
        return ret
