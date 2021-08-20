from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 8)
S = int(input())
MOD = 10 ** 9 + 7


@lru_cache(maxsize=10 ** 8)
def rec(n):
    if n < 3:
        return 0
    ret = 1
    for i in range(3, n - 3 + 1):
        ret += rec(i)
    return ret % MOD


print(rec(S))
