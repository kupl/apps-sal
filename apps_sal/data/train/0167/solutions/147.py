from functools import lru_cache
from typing import Tuple


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        return superEggHelper(K, N)


@lru_cache(maxsize=None)
def superEggHelper(K: int, N: int) -> int:
    if N == 0:
        return 0

    if K == 1:
        return N

    ans = bisectEggHelper(K, 1, N, N)

    return ans


def bisectEggHelper(K: int, S: int, E: int, N: int) -> int:
    if S == E:
        left, right = superEggCalc(K, S, N)
        return max(left, right) + 1

    if S + 1 == E:
        left1, right1 = superEggCalc(K, S, N)
        left2, right2 = superEggCalc(K, E, N)
        return min(max(left1, right1), max(left2, right2)) + 1

    i = (S + E) // 2
    left, right = superEggCalc(K, i, N)
    if left > right:
        return bisectEggHelper(K, S, i, N)
    else:
        return bisectEggHelper(K, i, E, N)


def superEggCalc(K: int, i: int, N: int) -> Tuple:
    return (superEggHelper(K - 1, i - 1), superEggHelper(K, N - i))
