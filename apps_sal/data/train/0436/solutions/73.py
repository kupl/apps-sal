import sys
sys.setrecursionlimit(1500000)
from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n, days,decrement=0):
            if decrement > 2:
                return math.inf
            if n==0:
                return days;

            best = 1e100
            best = min(best, helper(n-1,days+1,decrement+1))
            if n%2==0:
                best = min(best, helper(n-n/2, days+1))
            if n%3==0:
                best = min(best, helper(n-2*(n/3), days+1)) 
                           
            return best
                       
        return helper(n,0)
