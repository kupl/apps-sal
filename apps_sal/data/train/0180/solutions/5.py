class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if startFuel < target and (not stations):
            return -1
        dp = [startFuel] + [0] * len(stations)
        for (i, val) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= val[0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + val[1])
        for (i, d) in enumerate(dp):
            if d >= target:
                return i
        return -1
