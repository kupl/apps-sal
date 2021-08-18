class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        if startFuel >= target:
            return 0

        length = len(stations)
        dp = [startFuel] + [0] * length
        result = float('inf')
        for i in range(1 + length):
            for j in range(i, 0, -1):
                if dp[j - 1] >= stations[i - 1][0]:
                    dp[j] = max(dp[j], dp[j - 1] + stations[i - 1][1])

                if dp[j] >= target:
                    result = min(result, j)
        return -1 if result == float('inf') else result
