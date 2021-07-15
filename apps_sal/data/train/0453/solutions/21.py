class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houses = [c - 1 for c in houses]
        ans = [[[float('inf') for k in range(target+1)] for j in range(n)] for i in range(m)]
        
        
        for j in range(n):
            if houses[0] == -1:
                ans[0][j][1] = cost[0][j]
            else:
                ans[0][houses[0]][1] = 0

        for i in range(1, m):
            if houses[i] == -1:
                for j in range(n):
                    for l in range(n):
                        for k in range(1, min(target+1, i+2)):
                            if j == l:
                                ans[i][j][k] = min(ans[i][j][k], ans[i-1][j][k] + cost[i][j])
                            else:
                                ans[i][j][k] = min(ans[i][j][k], ans[i-1][l][k-1] + cost[i][j])
            else:
                for k in range(1, min(target+1, i+2)):
                    for l in range(n):
                        if houses[i] == l:
                            ans[i][houses[i]][k] = min(ans[i][houses[i]][k], ans[i-1][l][k])
                        else:
                            ans[i][houses[i]][k] = min(ans[i][houses[i]][k], ans[i-1][l][k-1])
                            
        res = float('inf')
        for j in range(n):
            res = min(res, ans[m-1][j][target])
        if res == float('inf'):
            res = -1
        return res
            
        
        
        

