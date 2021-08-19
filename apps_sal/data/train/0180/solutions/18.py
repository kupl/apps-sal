class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        N = len(stations)

        # We will try different number of stops. Initial state num_stops=0.
        # memo[num_stations] = max_mile we can reach if only available
        # first num_stations, and we make exactly num_stops

        prev_memo = [startFuel] * (N + 1)

        for num_stops in range(1, N + 1):
            memo = [-1] * (N + 1)

            a = -1
            for num_stations in range(num_stops, N + 1):
                station_mile, station_fuel = stations[num_stations - 1]
                # a = memo[num_stations - 1]
                # Optimization: a is available from previous loop,
                # so don't need to access it from memo[]
                b = prev_memo[num_stations - 1]
                if b >= station_mile:  # Check if we can reach this station
                    b += station_fuel
                    a = max(a, b)
                if a != -1:
                    memo[num_stations] = a

            # if memo[N] >= target:
            if a >= target:
                return num_stops

            prev_memo = memo

        return -1
