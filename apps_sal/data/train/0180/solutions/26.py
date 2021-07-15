
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        return self.dp(target, startFuel, stations)
    
    def dp(self, target, startFuel, stations):
        if startFuel >= target:
            return 0
        if not stations:
            return -1
        
        # A[t][i] = max distance using first i stations and stop t times (t<=i)
        # A[t][i] = max(
        #    A[t][i-1],
        #    A[t-1][i-1] + stations[i-1][1] if A[t-1][i-1] >= stations[i-1][0]
        
        n = len(stations)
        A = [[0] * (n+1) for _ in range(n+1)]
        
        for i in range(n+1):
            A[0][i] = startFuel
        
        for t in range(1, n+1):
            for i in range(1, n+1):
                if t <= i:
                    A[t][i] = A[t][i-1]
                    if A[t-1][i-1] >= stations[i-1][0]:
                        A[t][i] = max(A[t][i], A[t-1][i-1] + stations[i-1][1])
            if A[t][-1] >= target:
                return t
            
        return -1
    
    
    def rec1(self, target, startFuel, stations, position, station_idx_start):
        if position >= target or startFuel >= (target - position):
            #print(target, startFuel, stations, position)
            return 0
        else:
            candidates = []
            for idx in range(station_idx_start, len(stations)):
                p, f = stations[idx]
                d = p - position
                valid = d > 0 and startFuel - d >= 0
                if valid:
                    candidates.append(1 + self.rec(
                        target, 
                        startFuel - d + f, 
                        stations, 
                        p,
                        station_idx_start + 1))
                if startFuel - d < 0:
                    break
            
            if not candidates:
                return float('inf')
            else:
                return min(candidates)
