class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        rangesCovered = {}
        for (i, ran) in enumerate(ranges):
            if ran == 0:
                continue
            rangesCovered[i] = (max(0, i - ranges[i]), min(n, i + ranges[i]))
        dp = [n + 2] * (n + 1)
        dp[0] = 0
        for curRange in list(rangesCovered.values()):
            startInd = curRange[0]
            endInd = curRange[1]
            for i in range(startInd + 1, endInd + 1):
                dp[i] = min(dp[i], dp[startInd] + 1)
        if dp[n] == n + 2:
            return -1
        else:
            return dp[n]
