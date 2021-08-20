from sys import stdin
from functools import lru_cache
N = int(stdin.readline().rstrip())
K = int(stdin.readline().rstrip())


@lru_cache(None)
def f(N, K):
    if K < 0:
        return 0
    if N < 10:
        if K == 0:
            return 1
        elif K == 1:
            return N
        else:
            return 0
    (q, r) = divmod(N, 10)
    ret = 0
    if K >= 1:
        ret += f(q, K - 1) * r
        ret += f(q - 1, K - 1) * (9 - r)
    ret += f(q, K)
    return ret


print(f(N, K))
