class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp[i]: (a, b). a-> the longest distance a car can travel with i refuels
        #                b-> the location(distance) of fuels already used

        dp = [[startFuel, []]]
        for i in range(len(stations)):
            if dp[-1][0] >= target:
                break
            # print(\" \")
            # print(dp)
            usedStations = dp[-1][1]
            # print(usedStations)
            # reachable stations
            usable_stations = [s for s in stations if s[0] <= dp[-1][0] and s[0] not in usedStations]
            usable_stations.sort(key=lambda x: x[1])
            if len(usable_stations) == 0:
                break
            # print(usable_stations)
            dp.append([dp[-1][0] + usable_stations[-1][1], dp[-1][1].copy()])
            dp[-1][1].append(usable_stations[-1][0])

        return len(dp) - 1 if dp[-1][0] >= target else -1
