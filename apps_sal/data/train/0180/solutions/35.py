class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0

        if not stations:
            return -1

        dp = [startFuel]
        stops = 0
        lastd = 0
        for d, fuel in stations:
            for i in range(stops, len(dp)):
                dp[i] -= d - lastd
                if dp[i] < 0:
                    stops = i + 1

            if stops == len(dp):
                return -1

            dp.append(dp[-1] + fuel)
            for i in range(len(dp) - 2, stops, -1):
                dp[i] = max(dp[i], dp[i - 1] + fuel)

            if dp[stops] >= target - d:
                return stops

            lastd = d

        while stops < len(dp):
            if dp[stops] >= target - lastd:
                return stops
            stops += 1

        return -1
