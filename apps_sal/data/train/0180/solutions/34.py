class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target == startFuel:
            return 0

        stations = [startFuel] + stations
        dp = [0] * len(stations)
        dp[0] = (startFuel)
        for i in range(1, len(stations)):
            j = i - 1
            while j >= 0:
                totalFuel = dp[j] + stations[i][1]
                if dp[j] >= stations[i][0] and totalFuel >= dp[j + 1]:
                    dp[j + 1] = (totalFuel)
                j -= 1
        # print(dp)
        for i, fuel in enumerate(dp):
            if fuel >= target:
                return i
        return -1
