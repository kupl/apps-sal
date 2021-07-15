class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel = startFuel
        del startFuel
        i = 0
        while target > fuel:
            target -= fuel
            stations = [[dist-fuel, gas] for dist, gas in stations]
            try:
                j, fuel = max([[j, gas]
                               for j, (dist, gas) 
                               in enumerate(stations) 
                               if dist <= 0], 
                               key=lambda stop: stop[1])
            except ValueError:
                return -1
            if fuel == 0:
                return -1
            stations[j][1] = 0
            i += 1
        return i
