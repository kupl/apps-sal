class Solution:
    def minDays(self, n: int) -> int:
        
        @lru_cache(None)
        def eat(remaining, day):
            if remaining == 0:
                return day
            e3 = (
                eat(remaining - (2*remaining//3), day+1) if not remaining % 3 else
                eat(remaining - remaining % 3, day + remaining % 3)
            )
            e2 = (
                eat(remaining - (remaining//2),day+1) if not remaining % 2 else
                eat(remaining - 1, day + 1)
            )
            return min(e3, e2)
        
        return eat(n, 0)

