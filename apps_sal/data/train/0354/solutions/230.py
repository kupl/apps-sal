from functools import lru_cache


class Solution:
    def __init__(self):
        self.result = 0

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(last_val: int, streak_count: int, size: int):
            if size == n:
                return 1
            result = 0
            for i in range(len(rollMax)):
                if last_val != i:
                    result += helper(i, 1, size + 1)
                elif streak_count + 1 <= rollMax[i]:
                    result += helper(i, streak_count + 1, size + 1)
            return result
        return helper(-1, 1, 0) % (10**9 + 7)
