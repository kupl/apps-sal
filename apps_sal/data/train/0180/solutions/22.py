class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1
        data = []

        for k in range(len(stations)):
            data.append([stations[k][0] - (stations[k - 1][0] if k > 0 else 0), stations[k][1]])
        data.append([target - stations[-1][0], 0])

        tot = startFuel
        for dist, gas in data:
            tot -= dist
            if tot < 0:
                return -1
            tot += gas

        N = len(data)

        maxFuel = [float('-inf')] * N

        tot = startFuel
        for k in range(N):
            dist, _ = data[k]
            tot -= dist
            if tot < 0:
                break
            maxFuel[k] = tot

        nextMaxFuel = [float('-inf')] * N
        nextMaxFuel[0] = maxFuel[0] + data[0][1]
        for k in range(1, N):
            dist, gas = data[k]
            if maxFuel[k] != float('-inf'):
                nextMaxFuel[k] = maxFuel[k] + gas
            if nextMaxFuel[k - 1] >= dist:
                nextMaxFuel[k] = max(nextMaxFuel[k], nextMaxFuel[k - 1] - dist)
            if nextMaxFuel[k] == float('-inf'):
                break

        if nextMaxFuel[-1] >= 0:
            return 1

        maxFuel = nextMaxFuel

        for nStops in range(2, N + 1):
            nextMaxFuel = [float('-inf')] * N
            for k in range(nStops - 1, N):
                dist, gas = data[k]
                if maxFuel[k - 1] != float('-inf') and maxFuel[k - 1] >= dist:
                    nextMaxFuel[k] = maxFuel[k - 1] - dist + gas
                if nextMaxFuel[k - 1] >= dist:
                    nextMaxFuel[k] = max(nextMaxFuel[k], nextMaxFuel[k - 1] - dist)
                if nextMaxFuel[k] == float('-inf'):
                    break
            if nextMaxFuel[-1] >= 0:
                return nStops
            maxFuel = nextMaxFuel

        return -1
