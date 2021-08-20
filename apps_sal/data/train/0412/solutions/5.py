from functools import lru_cache


class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return memoization(d, f, target)


mod = 10 ** 9 + 7


@lru_cache(maxsize=None)
def memoization(d, f, t):
    if d == 0:
        return int(t == 0)
    return sum((memoization(d - 1, f, t - v) for v in range(1, f + 1))) % mod
