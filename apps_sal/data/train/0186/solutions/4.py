'''
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache
        def dfs(c, cur):
            #if c==0: print(c,cur)
            if c < 0: return 0
            if c == 0: return cur 
            ans = 0
            for i in range(9):
                ans = max(ans,dfs(c-cost[i], 10*cur+i+1))
            return ans
        return str(dfs(target, 0))
'''


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        '''
        from functools import lru_cache
        @lru_cache(None)
        def dfs(target,count):
            if target == 0:
                return 0

            res = -float(\"inf\")

            for i in range(len(cost)):
                if cost[i] <= target:
                    res = max(res, 10*dfs(target - cost[i], count+1)+i+1)


            return res

        res = dfs(target,0)

        return str(res) if res > 0 else \"0\"
        '''
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))
