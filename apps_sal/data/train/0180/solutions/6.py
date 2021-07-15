class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
#         if startFuel >= target:
#             return 0

#         @lru_cache(maxsize=None)
#         def helper(startIdx, litre, target):
#             if litre >= target:
#                 return 0

#             result = float('inf')
#             for idx in range(startIdx + 1, len(stations)):
#                 if startIdx == -1:
#                     n_miles = stations[idx][0]
#                 else:    
#                     n_miles = stations[idx][0] - stations[startIdx][0]

#                 remain = litre - n_miles
#                 if remain >= 0:
#                     result = min(result, 1 + helper(idx, remain + stations[idx][1], target - n_miles))
#             return result

#         result = helper(-1, startFuel, target)
#         return -1 if result == float('inf') else result

#-----------------------------------------------------------------------------

#         if startFuel >= target:
#             return 0

#         heap = []

#         idx = n_stations = 0
#         maxDistance = startFuel

#         while maxDistance < target:
#             while idx < len(stations) and stations[idx][0] <=maxDistance:
#                 heapq.heappush(heap, -stations[idx][1])
#                 idx += 1

#             if not heap:
#                 return -1

#             maxDistance += (-heapq.heappop(heap))
#             n_stations += 1
#         return n_stations

#-----------------------------------------------------------------------------

#         if startFuel >= target:
#             return 0

#         length = len(stations)
#         dp = [[0] * (1 + length) for _ in range(1 + length)]
#         for i in range(1 + length):
#             dp[i][0] = startFuel

#         result = float('inf')
#         for i in range(1 + length):
#             for j in range(1, i + 1):
#                 if j <= i - 1:
#                     dp[i][j] = max(dp[i][j], dp[i - 1][j])

#                 if dp[i - 1][j - 1] >= stations[i - 1][0]:
#                     dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + stations[i - 1][1])

#                 if dp[i][j] >= target:
#                     result = min(result, j)
#         return -1 if result == float('inf') else result

#-----------------------------------------------------------------------------
        
        if startFuel >= target:
            return 0
        
        length = len(stations)
        dp = [startFuel] + [0] * length
        result = float('inf')
        for i in range(1 + length):
            for j in range(i, 0, -1):
                if dp[j - 1] >= stations[i - 1][0]:
                    dp[j] = max(dp[j], dp[j - 1] + stations[i - 1][1])

                if dp[j] >= target:
                    result = min(result, j)
        return -1 if result == float('inf') else result
