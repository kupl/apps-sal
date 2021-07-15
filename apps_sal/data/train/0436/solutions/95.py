import sys
sys.setrecursionlimit(1500000)
class Solution:
    def minDays(self, n: int) -> int:
        # 我当时看到数据范围n觉得直接dp(n)会超时因此我就没做。
        # 但是实际上每次都是整除2整除3其实只需要log(n)时间就搞定！
        @lru_cache(None)
        def go(x):
            if x == 0:
                return 0
            
            best = 1e100
            if x % 2 == 0:
                best = min(best, go(x // 2) + 1)
            if x % 3 == 0:
                best = min(best, go(x // 3) + 1)
            
            if x <= (1024) or x % 2 > 0 or x % 3 > 0:
                best = min(best, go(x - 1) + 1)
                
            return best
        return go(n)
        '''
        @lru_cache(None)
        def dp(x):
            if x <= 1: return x
            res = x
            res = min(res, dp(x//3) + x % 3 + 1)
            res = min(res, dp(x//2) + x % 2 + 1)
            return res
        return dp(n)
        '''
