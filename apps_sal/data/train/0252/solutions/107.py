class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        coords = []
        for (i, rng) in enumerate(ranges):
            if not rng:
                continue
            coords.append([max(0, i - rng), min(i + rng, n)])
        coords.sort()
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for [start, end] in coords:
            if start > n:
                break
            prev = dp[start]
            for i in range(start, min(end, n)):
                dp[i + 1] = min(prev + 1, dp[i + 1])
        return dp[-1] if dp[-1] < float('inf') else -1
