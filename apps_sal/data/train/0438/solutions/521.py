import bisect
import collections
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        intervals = []
        lengths = collections.defaultdict(int)
        ans = -1
        for step, x in enumerate(arr):
            ind = bisect.bisect(intervals, [x, x])
            intervals.insert(ind, [x, x])
            lengths[1] += 1
            merge_left = merge_right = ind
            if ind - 1 >= 0 and intervals[ind - 1][1] == x - 1:
                merge_left = ind - 1
            if ind + 1 < len(intervals) and intervals[ind + 1][0] == x + 1:
                merge_right = ind + 1
            # print(intervals)
            if merge_right > merge_left:
                for i in range(merge_left, merge_right + 1):
                    lengths[intervals[i][1] - intervals[i][0] + 1] -= 1
                lengths[intervals[merge_right][1] - intervals[merge_left][0] + 1] += 1
                intervals[merge_left:merge_right + 1] = [[intervals[merge_left][0], intervals[merge_right][1]]]
            if lengths[m] > 0:
                ans = step + 1
            # print(step, x)
            # print(intervals,lengths)

        return ans
