class Solution:

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        res = [Interval(intervals[0].start, intervals[0].end)]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[len(res) - 1].end:
                res[len(res) - 1].start = min(res[len(res) - 1].start, intervals[i].start)
                res[len(res) - 1].end = max(res[len(res) - 1].end, intervals[i].end)
            else:
                res.append(Interval(intervals[i].start, intervals[i].end))
        return res
