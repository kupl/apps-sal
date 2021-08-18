from functools import lru_cache

mapping = [
    [4, 6],
    [6, 8],
    [7, 9],
    [4, 8],
    [0, 3, 9],
    [],
    [0, 1, 7],
    [2, 6],
    [1, 3],
    [2, 4]
]

mod = 1000_000_007


@lru_cache(None)
def dfs(n, i):
    if n == 1:
        return 1

    sum_ = 0
    for nei in mapping[i]:
        sum_ = (sum_ + dfs(n - 1, nei)) % mod

    return sum_


class Solution:
    def knightDialer(self, N: int) -> int:
        total = 0
        for i in range(10):
            total = (total + dfs(N, i)) % mod

        return total
