import functools


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted((get_power_value(x), x) for x in range(lo, hi + 1))[k - 1][1]


@functools.lru_cache(maxsize=None)
def get_power_value(x):
    if x == 1:
        return 0
    return 1 + get_power_value(x / 2 if x % 2 == 0 else x * 3 + 1)
