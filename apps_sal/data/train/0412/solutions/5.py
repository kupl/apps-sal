from functools import lru_cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return memoization(d, f, target)

# thank goodness that dices have orders (they are different dices)
# d = 2, f = 3, t = 4
# (1,3), (2,2), (3,1)
# note that (1,3) and (3,1) are different ways (by definition in this example)
# TODO: what if they are exchangable?

# sol:
# f(d, f, t) = f(d-1, f, t-v) for v ...


mod = 10**9 + 7


@lru_cache(maxsize=None)
def memoization(d, f, t):
    if d == 0:
        return int(t == 0)
    return sum(memoization(d - 1, f, t - v) for v in range(1, f + 1)) % mod
