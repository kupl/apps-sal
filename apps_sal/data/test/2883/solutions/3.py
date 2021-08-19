class Solution:

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        if not start:
            return end
        if not end:
            return start
        result = list()
        make_interval = 1
        (i, j) = (1, 0)
        first_start = 0
        while i < len(start) and j < len(end):
            if start[i] <= end[j]:
                make_interval += 1
                i += 1
            else:
                make_interval -= 1
                if make_interval == 0:
                    result.append([start[first_start], end[j]])
                    first_start = i
                j += 1
        if j < len(end):
            result.append([start[first_start], end[-1]])
        return result
