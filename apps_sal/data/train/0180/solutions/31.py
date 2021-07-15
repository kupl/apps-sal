from functools import lru_cache


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        @lru_cache(None)
        def farthest_of_first_n_with_stops(n, stops):
            if n == 0 or stops == 0:
                return startFuel

            dont_refuel_now = farthest_of_first_n_with_stops(n - 1, stops)
            refuel_now = farthest_of_first_n_with_stops(n - 1, stops - 1)
            x, fuel = stations[n - 1]
            if refuel_now < x:  # can't reach stations[n - 1]
                return dont_refuel_now
            else:
                return max(dont_refuel_now, fuel + refuel_now)

        for stops in range(len(stations) + 1):
            # print(farthest_of_first_n_with_stops(len(stations), stops))
            if farthest_of_first_n_with_stops(len(stations), stops) >= target:
                return stops

        return -1

