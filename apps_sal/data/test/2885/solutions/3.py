class Solution:

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans = []
        if intervals == []:
            return [newInterval]
        elif newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        elif newInterval.start > intervals[-1].end:
            return intervals + [newInterval]
        new_start = newInterval.start
        new_end = newInterval.end
        for i in range(0, len(intervals)):
            if intervals[i].end < new_start:
                ans.append(intervals[i])
            elif i and intervals[i - 1].end < new_start and (new_end < intervals[i].start):
                ans.append(newInterval)
                for j in range(i, len(intervals)):
                    ans.append(intervals[j])
                return ans
            else:
                merge_start = min(intervals[i].start, new_start)
                merge_end = max(intervals[i].end, new_end)
                break
        notStop = 1
        for ii in range(i + 1, len(intervals)):
            if intervals[ii].start > merge_end:
                notStop = 0
                break
        if notStop:
            merge_end = max(intervals[-1].end, merge_end)
            ans.append(Interval(merge_start, merge_end))
            return ans
        merge_end = max(intervals[ii - 1].end, merge_end)
        ans.append(Interval(merge_start, merge_end))
        for iii in range(ii, len(intervals)):
            ans.append(intervals[iii])
        return ans
