class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0
        dpRefuels = [[-1] * len(stations) for _ in range(len(stations))]
        for i in range(len(stations)):
            if stations[i][0] <= startFuel:
                dpRefuels[0][i] = stations[i][1] + startFuel
                if dpRefuels[0][i] >= target:
                    return 1

        for k in range(1, len(stations)):
            maxPrevFuel = dpRefuels[k - 1][k - 1]
            for i in range(k, len(stations)):
                if maxPrevFuel >= stations[i][0]:
                    dpRefuels[k][i] = maxPrevFuel + stations[i][1]
                if dpRefuels[k][i] >= target:
                    return k + 1
                maxPrevFuel = max(maxPrevFuel, dpRefuels[k - 1][i])
        return -1
