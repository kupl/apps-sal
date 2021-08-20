from functools import lru_cache


class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        moves = [-1, 0, 1]

        @lru_cache(maxsize=2048)
        def count(s, position=0):
            if position < 0 or position >= arrLen:
                return 0
            if s == 0:
                return 1 if position == 0 else 0
            number_of_moves = 0
            for delta in moves:
                new_position = position + delta
                number_of_moves += count(s - 1, new_position)
            return number_of_moves
        return count(steps) % (10 ** 9 + 7)
