class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for row in dp:
            row[0] = startFuel
    
        if startFuel >= target: return 0
        
        for refuels in range(1, n+1):
            for stas in range(1, n+1):
                station = stations[stas-1]
                dp[stas][refuels] = dp[stas-1][refuels]
                if dp[stas-1][refuels-1] >= station[0]:
                    dp[stas][refuels] = max(station[1] + dp[stas-1][refuels-1], dp[stas][refuels])

            if dp[n][refuels] >= target: return refuels
            
        return -1
    
    
    
    
    
#             for refue in range(1, n + 1):
#             for station in range(1, n + 1):
#                 dp[station][refue] = dp[station - 1][refue]
#                 if dp[station - 1][refue - 1] >= stations[station - 1][0]:
#                     dp[station][refue] = max(dp[station - 1][refue - 1] + stations[station - 1][1], dp[station][refue])
                
#             if dp[n][refue] >= target:
#                 return refue
        
#         return -1

