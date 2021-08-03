# [Runtime: 1212 ms, faster than 5.27%] DP
#O(N * 200)
# f(i): the minimum number of taps that we can cover range: 0~i and i is opended
# Since 0~n is already sorted sequence of number
# f(i) = 1 if ranges[i][BEGIN] <= 0
# f(i) = min( f(j) where max(0, ranges[i][BEGIN]-100) <= j < i and ranges[j][END] >= ranges[i][BEGIN] ) + 1
# NOTE: WA: return min { f(i) if i + ranges[i][END] >= n }
from math import inf


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [inf] * (n + 1)
        for i in range(n + 1):
            if not ranges[i]:
                continue  # skip impossible tapes to prevent from empty arg of `min`
            s = i - ranges[i]
            if s <= 0:
                dp[i] = 1
            else:
                dp[i] = 1 + min([dp[j] for j in range(max(0, s - 100), i) if ranges[j] and j + ranges[j] >= s] + [inf])
        res = min([dp[i] for i in range(n + 1) if ranges[i] and i + ranges[i] >= n] + [inf])
        return res if res != inf else -1
