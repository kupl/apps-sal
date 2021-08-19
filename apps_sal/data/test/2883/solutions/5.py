class Solution:

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length == 1 or length == 0:
            return intervals
        intervals.sort(key=lambda l: l.start)
        result = []
        curr = intervals.pop(0)
        while intervals:
            next_int = intervals.pop(0)
            if curr.end >= next_int.start:
                if curr.end < next_int.end:
                    curr.end = next_int.end
            else:
                result.append(curr)
                curr = next_int
        result.append(curr)
        return result
