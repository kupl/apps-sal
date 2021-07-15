from functools import lru_cache
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def dfs(residual, last, lastFre):
            if residual == 0:
                return 1
            tmp = 0
            if rollMax[last - 1] == lastFre:
                for i in range(6):
                    if i + 1 == last:
                        continue
                    tmp += dfs(residual - 1, i + 1, 1) % (10**9 + 7)
            else:
                for i in range(6):
                    if i + 1 == last:
                        tmp += dfs(residual - 1, last, lastFre + 1)% (10**9 + 7)
                    else:
                        tmp += dfs(residual - 1, i + 1, 1)% (10**9 + 7)
            return tmp % (10**9 + 7)
        
        ans = 0
        for j in range(1, 7):
            ans += dfs(n-1, j, 1)
            ans %=  (10**9 + 7)
        return ans 

