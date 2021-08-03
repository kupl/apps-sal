from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        intervals = {}
        lengths = defaultdict(int)

        found = -1
        for i, val in enumerate(arr):
            if (val - 1) not in intervals and (val + 1) not in intervals:
                intervals[val] = val
                lengths[1] += 1

            if (val - 1) in intervals and (val + 1) not in intervals:
                prev_left = intervals[val - 1]
                prev_right = val - 1
                lengths[prev_right - prev_left + 1] -= 1
                lengths[prev_right - prev_left + 2] += 1

                intervals[prev_left] = val
                intervals[val] = prev_left

            if (val - 1) not in intervals and (val + 1) in intervals:
                prev_right = intervals[val + 1]
                prev_left = val + 1
                lengths[prev_right - prev_left + 1] -= 1
                lengths[prev_right - prev_left + 2] += 1

                intervals[prev_right] = val
                intervals[val] = prev_right

            if (val - 1) in intervals and (val + 1) in intervals:
                prev_right = intervals[val + 1]
                prev_left = intervals[val - 1]

                lengths[prev_right - val] -= 1
                lengths[val - prev_left] -= 1
                lengths[prev_right - prev_left + 1] += 1

                intervals[prev_left] = prev_right
                intervals[prev_right] = prev_left
                if val + 1 != prev_right:
                    del intervals[val + 1]
                if val - 1 != prev_left:
                    del intervals[val - 1]

            if lengths[m] != 0:
                found = i + 1

        return found
