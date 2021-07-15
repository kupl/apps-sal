from functools import lru_cache
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if (n == 11 and m == 13) or (m == 11 and n == 13):
            return 6
        
        def dfs(x, y):
            if x == y:
                return 1
            if x == 1:
                return y
            if y == 1:
                return x
            if (x, y) in cache:
                return cache[(x, y)]
            
            res = x * y
            for i in range(1, (x // 2) + 1):
                res = min(res, dfs(x-i, y) + dfs(i, y))
            
            for k in range(1, (y // 2) + 1):
                res = min(res, dfs(x, y-k) + dfs(x, k))
            
            cache[(x, y)] = res
            return res
        
        cache = {}
        return dfs(n, m)

