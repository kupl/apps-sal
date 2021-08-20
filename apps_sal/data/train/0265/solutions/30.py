from collections import defaultdict
from bisect import *


class Solution:

    def maxNonOverlapping(self, lst: List[int], k: int) -> int:
        n = len(lst)
        first = 0
        last = 0
        total = lst[0]
        dct = defaultdict(list)
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + lst[i - 1]
            dct[dp[i]].append(i)
        intervals = []
        for i in range(n + 1):
            left = bisect_right(dct[k + dp[i]], i)
            if left != len(dct[k + dp[i]]):
                intervals.append((i, dct[k + dp[i]][left]))
        intervals.sort(key=lambda x: x[1])
        pre = -float('inf')
        ans = 0
        index = 0
        print(intervals)
        while index < len(intervals):
            if intervals[index][0] >= pre:
                ans += 1
                pre = intervals[index][1]
            index += 1
        return ans
