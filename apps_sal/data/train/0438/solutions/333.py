import bisect
import math


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = [i - 1 for i in arr]
        splitted = [(0, len(arr) - 1)]
        step = len(arr)
        if len(arr) == m:
            return step
        for n in reversed(arr):
            step -= 1
            i = bisect.bisect_right(splitted, (n, math.inf))
            range_ = splitted[i - 1]
            left = (range_[0], n - 1)
            right = (n + 1, range_[1])
            if left[1] - left[0] + 1 == m or right[1] - right[0] + 1 == m:
                return step
            replace = []
            if left[1] >= left[0]:
                replace.append(left)
            if right[1] >= right[0]:
                replace.append(right)
            splitted[i - 1:i] = replace
        return -1
