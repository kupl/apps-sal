
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []:
            return [newInterval]

        index = 0
        while index < len(intervals):
            if newInterval.start < intervals[index].start:
                break
            index += 1
        del_index = 0
        insert_index = 0
        if index == 0:
            s = newInterval.start
            e = newInterval.end
            insert_index = index
        else:
            if newInterval.start <= intervals[index - 1].end:
                s = intervals[index - 1].start
                e = max(intervals[index - 1].end, newInterval.end)
                insert_index = index - 1
                del_index += 1
            else:
                s = newInterval.start
                e = newInterval.end
                insert_index = index

        while index < len(intervals):
            if intervals[index].start <= e:
                e = max(e, intervals[index].end)
                del_index += 1
                index += 1
            else:
                break
        i = 0
        while i < del_index:
            intervals.pop(insert_index)
            i += 1
        intervals.insert(insert_index, Interval(s, e))
        return intervals
