from functools import lru_cache
mapping = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
mod = 1000000007


@lru_cache(None)
def f(n: int, d: int) -> int:
    if n == 1:
        return 1
    s = 0
    for d1 in mapping[d]:
        s = (s + f(n - 1, d1)) % mod
    return s


class Solution:

    def knightDialer(self, N: int) -> int:
        tot = 0
        for d in range(10):
            tot = (tot + f(N, d)) % mod
        return tot
