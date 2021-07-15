class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        stations.append([target, 0])
        stations.sort(reverse=True)
        curr, tank = 0, startFuel
        ans = 0
        refuels = []
        while curr + tank < target:
            pos, gas = stations.pop()
            if pos <= curr+tank:
                heapq.heappush(refuels, -gas)
            else:
                curr += tank
                tank = 0
                while curr+tank < pos and refuels:
                    ans += 1
                    tank -= heapq.heappop(refuels)
                if curr+tank < pos:
                    return -1
                heapq.heappush(refuels, -gas)
        return ans
