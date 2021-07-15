import functools

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def can_force_win_from(m):
            if m == 0:
                return False
            if m == 1:
                return True

            for root in range(1, int(m ** 0.5) + 1):
                if not can_force_win_from(m - root * root):
                    return True
            return False
        return can_force_win_from(n)

