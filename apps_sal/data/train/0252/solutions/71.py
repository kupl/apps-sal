from typing import List, Tuple
from sortedcontainers import SortedSet


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # print('-----')
        # print(f'n: {n}')
        # print(f'ranges: {ranges}')

        intervals = SortedSet()

        for i, w in enumerate(ranges):
            newInterval = (max(i - w, 0), min(i + w, n))
            idx = intervals.bisect_left(newInterval)

            if idx < len(intervals) and self.aContainsB(intervals[idx], newInterval):
                continue
            elif idx > 0 and self.aContainsB(intervals[idx-1], newInterval):
                continue
            else:
                change = True
                while change:
                    change = False
                    idx = intervals.bisect_left(newInterval)
                    if idx < len(intervals) and self.aContainsB(newInterval, intervals[idx]):
                        del intervals[idx]
                        change = True
                    elif idx > 0 and self.aContainsB(newInterval, intervals[idx-1]):
                        del intervals[idx-1]
                        change = True
                    elif idx > 1 and self.overlaps(newInterval, intervals[idx-2]):
                        del intervals[idx-1]
                        change = True
                intervals.add(newInterval)

        # print(f'intervals={intervals}')

        prevEnd = 0
        for (start, end) in intervals:
            if start > prevEnd:
                return -1
            prevEnd = end
        if end < n:
            return -1

        return len(intervals)

    def aContainsB(self, a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        a_start, a_end = a
        b_start, b_end = b
        return a_start <= b_start and a_end >= b_end

    def overlaps(self, a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        a_start, a_end = a
        b_start, b_end = b
        return a_end >= b_start and b_end >= a_start

