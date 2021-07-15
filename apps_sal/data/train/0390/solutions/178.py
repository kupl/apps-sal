class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        from functools import lru_cache
        @lru_cache(None)
        def can_win(remain):
            if remain == 0:
                return False
            
            root = 1
            while root**2 <= remain:
                if not can_win(remain - root**2):
                    return True
                root += 1
            return False
        
        return can_win(n)
