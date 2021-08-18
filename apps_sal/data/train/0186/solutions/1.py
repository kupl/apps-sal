class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def dfs(c):
            if c == 0:
                return 0
            ans = -float('inf')
            for i in range(9):
                if cost[i] <= c:
                    ans = max(ans, 10 * dfs(c - cost[i]) + i + 1)
            return ans
        res = dfs(target)
        return str(res) if res > 0 else '0'


'''
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(target):
            if target == 0: return 0
            res = -float(\"inf\")
            for i in range(len(cost)):
                if cost[i] <= target:
                    res = max(res, 10*dfs(target - cost[i])+i+1)
            return res
        res = dfs(target)
        return str(res) if res > 0 else \"0\"
'''
