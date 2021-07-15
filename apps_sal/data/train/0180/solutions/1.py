class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1

        fdelta = startFuel-stations[0][0]
        if fdelta < 0:
            return -1

        curr = [fdelta + stations[0][1], fdelta]

        for i, sta in enumerate(stations[1:]):
            treck = sta[0] - stations[i][0]
            leftover = curr[0]-treck
            if leftover < 0:
                return -1
            nex = [leftover + sta[1], leftover]
            for j, f in enumerate(curr[1:]):
                leftover = curr[j+1] - treck
                if leftover < 0:
                    break
                else:
                    nex[-1] = max(nex[-1], leftover+sta[1])
                    nex.append(leftover)

            curr = nex

        leftover = target - stations[-1][0]

        while curr and curr[-1] < leftover:
            curr.pop()

        return len(stations) - len(curr) + 1 if curr else -1
