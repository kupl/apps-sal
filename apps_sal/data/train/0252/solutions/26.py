class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        res = 0
        DP = [float('inf')] * (n + 1)
        farest = 0
        DP[0] = 0
        for (i, r) in enumerate(ranges):
            for x in range(max(i - r, 0), min(i + r + 1, n + 1)):
                DP[x] = min(DP[x], DP[max(i - r, 0)] + 1)
        return DP[-1] if DP[-1] != float('inf') else -1
