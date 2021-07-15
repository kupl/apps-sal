from collections import defaultdict
from math import inf
from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr2)
        dp = {-1: 0}
        for i in arr1:
            next_dp = defaultdict(lambda: inf)
            for key in dp:
                if i > key:
                    next_dp[i] = min(next_dp[i], dp[key])
                loc = bisect_right(arr2, key)
                if loc < n:
                    next_dp[arr2[loc]] = min(next_dp[arr2[loc]], dp[key] + 1)
            dp = next_dp

        return min(dp.values()) if dp else -1
