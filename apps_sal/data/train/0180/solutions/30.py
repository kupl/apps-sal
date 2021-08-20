class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0
        dp = [[0 for _ in range(len(stations) + 1)] for _ in range(len(stations) + 1)]
        for i in range(len(stations) + 1):
            dp[i][0] = startFuel
        for i in range(1, len(stations) + 1):
            for j in range(1, len(stations) + 1):
                dp[j][i] = dp[j - 1][i]
                if dp[j - 1][i - 1] >= stations[j - 1][0]:
                    dp[j][i] = max(dp[j][i], dp[j - 1][i - 1] + stations[j - 1][1])
            if dp[j][i] >= target:
                return i
        return -1
