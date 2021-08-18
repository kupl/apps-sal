class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        N = len(stations)

        prev_memo = [startFuel] * (N + 1)

        for num_stops in range(1, N + 1):
            memo = [-1] * (N + 1)

            a = -1
            for num_stations in range(num_stops, N + 1):
                station_mile, station_fuel = stations[num_stations - 1]
                b = prev_memo[num_stations - 1]
                if b >= station_mile:
                    a = max(a, b + station_fuel)
                if a != -1:
                    memo[num_stations] = a

            if a >= target:
                return num_stops

            prev_memo = memo

        return -1
