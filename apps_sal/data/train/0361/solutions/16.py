class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
       
        @lru_cache
        def dp(x = n, y = m):
            if x == y:
                return 1
            r = m * n
            for i in range(1, x//2 + 1):
                r = min(r, dp(i, y) + dp(x - i, y))
            for k in range(1, y//2 + 1):
                r = min(r, dp(x, k) + dp(x, y - k))
            for l in range(1, min(x, y)):
                for i in range(1, x - l):
                    for k in range(1, y - l):
                        p1 = dp(i + l, k)
                        p2 = dp(x - i - l, l + k)
                        p3 = dp(i, y - k)
                        p4 = dp(x - i, y - k - l)
                        r = min(r, p1 + p2 + p3 + p4 + 1)
                        
                        
            return r
            
        return dp()
