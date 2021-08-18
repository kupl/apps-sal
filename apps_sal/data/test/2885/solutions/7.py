
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left = 0
        right = len(intervals) - 1
        tar = newInterval.start
        while True:
            if left > right:
                break
            mid = (left + right) // 2
            value = intervals[mid].start
            if value == tar:
                left = mid
                break
            elif value > tar:
                right = mid - 1
            else:
                left = mid + 1
        intervals.insert(left, newInterval)
        ret = []
        tmp = intervals[0]
        ret.append(tmp)
        it = iter(intervals)
        next(it)
        for i in it:
            if i.start <= ret[-1].end:
                prev = ret.pop()
                ret.append(Interval(prev.start, max(i.end, prev.end)))
            else:
                ret.append(i)
        return ret
