class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [-1 for x in range(n + 1)]
        for i in range(n + 1):
            minId = max(0, i - ranges[i])
            maxId = min(n, i + ranges[i])
            for i in range(minId, maxId + 1):
                dp[i] = max(dp[i], maxId)
        if dp[0] == -1:
            return -1
        maxReach = dp[0]
        count = 1
        while maxReach < n:
            nxt = dp[maxReach]
            if nxt == maxReach:
                return -1
            maxReach = nxt
            count += 1
        return count
