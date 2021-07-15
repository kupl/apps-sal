class Solution:
    def minDays(self, n: int) -> int:
        
        self.best = math.inf
        
        @lru_cache(None)
        def f(n, steps):
            if n == 0:
                self.best = min(self.best, steps)
                return steps
            
            if steps > self.best:
                return math.inf
            ans = math.inf
            if n % 3 == 0:
                ans = min(ans, f(n // 3, steps + 1))
            if n % 2 == 0:
                ans = min(ans, f(n // 2, steps + 1))

            ans = min(ans, f(n-1, steps + 1))
            return ans
        
        return f(n, 0)
