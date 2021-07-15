class Solution:
    def minDays(self, n: int) -> int:
        
        @lru_cache(None)
        def days(m: int, steps: int):
            nonlocal maxSteps
            if steps >= maxSteps:
                return
            if m == 0:
                maxSteps = steps
            if m > 0:
                if m % 3 == 0:
                    days(m // 3, steps + 1)
                if m % 2 == 0:
                    days(m // 2, steps + 1)
                days(m - 1, steps + 1)
             
        maxSteps = n
        days(n, 0)
        return maxSteps
