class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        #dp[house][target][color]
        dp = [[[float('inf')]*(n+1) for j in range(target+1)] for i in range(m)]
        
        if houses[0] == 0:
            for idx, c in enumerate(cost[0]):
                dp[0][1][idx+1] = c
        else:
            dp[0][1][houses[0]] = 0
            
        for i in range(1, m):
            if houses[i] != 0:
                for t in range(1, target+1):
                    for cidx in range(1, n+1):
                        pre_cost = dp[i-1][t][cidx]
                        if pre_cost == float('inf'):
                            continue
                        if houses[i] == cidx:
                            dp[i][t][cidx] = min(dp[i][t][houses[i]], pre_cost)
                        elif t + 1 <= target:
                            dp[i][t + 1][houses[i]] = min(dp[i][t+1][houses[i]], pre_cost)
            else:
                for t in range(1, target+1):
                    for cidx in range(1, n+1):
                        pre_cost = dp[i-1][t][cidx]
                        if pre_cost == float('inf'):
                            continue
                        for cidx2, c in enumerate(cost[i]):
                            cidx2+=1
                            if cidx == cidx2:
                                dp[i][t][cidx2] = min(dp[i][t][cidx2], pre_cost + c)
                            elif t +1 <= target:
                                dp[i][t+1][cidx2] = min(dp[i][t+1][cidx2], pre_cost + c)
        #print(dp)
        res = float('inf')
        for cidx in range(1, n+1):
            res = min(res, dp[-1][target][cidx])
            
        if res == float('inf'):
            return -1
        return res
                                

