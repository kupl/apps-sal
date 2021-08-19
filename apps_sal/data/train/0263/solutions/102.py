from functools import lru_cache

mapping = [
    [4, 6],  # 0
    [6, 8],  # 1
    [7, 9],  # 2
    [4, 8],  # 3
    [0, 3, 9],  # 4
    [],  # 5
    [0, 1, 7],  # 6
    [2, 6],  # 7
    [1, 3],  # 8
    [2, 4]  # 9
]

mod = 1000_000_007


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
