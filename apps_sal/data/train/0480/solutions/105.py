class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modulo = 10**9 + 7

        @lru_cache(None)
        def make_step(pos, steps_left):
            if steps_left == 0 or pos > steps_left:
                if pos == 0:
                    return 1
                return 0
            else:
                # Left
                ways = 0
                if pos > 0:
                    ways += make_step(pos - 1, steps_left - 1) % modulo
                # Right
                if pos < arrLen - 1:
                    ways += make_step(pos + 1, steps_left - 1) % modulo
                # Stay
                ways += make_step(pos, steps_left - 1) % modulo
                return ways % modulo

        return make_step(0, steps)
