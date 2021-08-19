from math import inf


class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [inf] * (n + 1)
        for i in range(n + 1):
            if not ranges[i]:
                continue
            s = i - ranges[i]
            if s <= 0:
                dp[i] = 1
            else:
                dp[i] = 1 + min([dp[j] for j in range(max(0, s - 100), i) if ranges[j] and j + ranges[j] >= s] + [inf])
        res = min([dp[i] for i in range(n + 1) if ranges[i] and i + ranges[i] >= n] + [inf])
        return res if res != inf else -1
