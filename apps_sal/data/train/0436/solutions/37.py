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
            if n % 3 == 0:
                f(n // 3, steps + 1)
            if n % 2 == 0:
                f(n // 2, steps + 1)

            f(n-1, steps + 1)
        
        f(n, 0)
        return self.best
