class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # f[i,j], the maximum full one can have, using j stations, stop at station i,
        # f[i,j] = f[i],  j implied by iteration
        if target <= startFuel:
            return 0

        stations = [[0, startFuel]] + stations
        print(stations)
        N = len(stations)
        f = [startFuel - stations[i][0] for i in range(N)]
        f[0] = startFuel

        print(f)
        for j in range(N):
            g = [-1] * (N)
            g[0] = f[0]
            for i in range(N - 1, 0, -1):
                if f[i - 1] - (stations[i][0] - stations[i - 1][0]) >= 0:
                    g[i] = f[i - 1] + stations[i][1] - (stations[i][0] - stations[i - 1][0])

            for i in range(1, N):
                g[i] = max(g[i - 1] - (stations[i][0] - stations[i - 1][0]), g[i])

            f = g
            if f[-1] >= (target - stations[-1][0]):
                return j + 1

        return -1
