class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def solve(s: int, stops: int) -> int:
            if stops == 0 or s < 0:
                return startFuel

            return max(solve(s - 1, stops), (sub + stations[s][1]) if (sub := solve(s - 1, stops - 1)) >= stations[s][0] else 0)

        for i in range(len(stations) + 1):
            if solve(len(stations) - 1, i) >= target:
                return i

        return -1
