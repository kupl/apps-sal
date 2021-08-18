class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for row in dp:
            row[0] = startFuel

        if startFuel >= target:
            return 0

        for refuels in range(1, n + 1):
            for stas in range(1, n + 1):
                station = stations[stas - 1]
                dp[stas][refuels] = dp[stas - 1][refuels]
                if dp[stas - 1][refuels - 1] >= station[0]:
                    dp[stas][refuels] = max(station[1] + dp[stas - 1][refuels - 1], dp[stas][refuels])

            if dp[n][refuels] >= target:
                return refuels

        return -1
