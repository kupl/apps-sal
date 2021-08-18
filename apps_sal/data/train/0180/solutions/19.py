class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0
        dpRefuels = [-1] * len(stations)
        for i in range(len(stations)):
            if stations[i][0] <= startFuel:
                dpRefuels[i] = stations[i][1] + startFuel
                if dpRefuels[i] >= target:
                    return 1

        for k in range(1, len(stations)):
            maxPrevFuel = dpRefuels[k - 1]
            for i in range(k, len(stations)):
                temp = max(maxPrevFuel, dpRefuels[i])
                if maxPrevFuel >= stations[i][0]:
                    dpRefuels[i] = maxPrevFuel + stations[i][1]
                if dpRefuels[i] >= target:
                    return k + 1
                maxPrevFuel = temp

        return -1
