class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        '''
        houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
        Output: 9
        
        [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
        
        if cur_t == target: same as pre
        if cur_t < target: new or same as pre
        
        dp(i, cur_t) = 
        if memo
        res = float('inf')
        if i == len(houses):
            if cur_t == target: return 0
            else: return res
        if cur_t > target: return res
        
        if houses[i] != 0:
            if i>0 and houses[i] == houses[i-1]:
                res = dp(i+1, cur_t)
            else: res = dp(i+1, cur_t+1)
        else:
            for color in range(1,n+1):
                if i>0 and color = houses[i-1]:
                    houses[i] = color
                    res = min(res, cost[i][color-1] + dp(i+1, cur_t))
                    houses[i] = 0
                else:
                    houses[i] = color
                    res = min(res, cost[i][color-1] + dp(i+1, cur_t+1))
                    houses[i] = 0
            
        
        
        '''
        memo = {}
        def dp(i, pre_col, cur_t):
            # print(i, cur_t)
            res = float('inf')
            if i == len(houses):
                if cur_t == 0: return 0
                else: return res
            if cur_t < 0: return res
            if (i, pre_col,cur_t) in memo.keys(): return memo[(i, pre_col,cur_t)]
            
            if houses[i] != 0:
                if i>0 and houses[i] == pre_col:
                    res = dp(i+1, pre_col, cur_t)
                else: res = dp(i+1, houses[i], cur_t-1)
            else:
                for color in range(1,n+1):
                    if i>0 and color == pre_col:
                        # houses[i] = color
                        res = min(res, cost[i][color-1] + dp(i+1, pre_col,cur_t))
                        # houses[i] = 0
                    else:
                        # houses[i] = color
                        res = min(res, cost[i][color-1] + dp(i+1,color, cur_t-1))
                        # houses[i] = 0
            memo[(i,pre_col, cur_t)] = res
            return res
        ans = dp(0, houses[0],target)
        return ans if ans != float('inf') else -1
