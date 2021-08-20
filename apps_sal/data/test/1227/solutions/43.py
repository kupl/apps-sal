import sys
from functools import lru_cache
N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())


@lru_cache(None)
def F(N, K):
    """(0以上）N以下で、0でないものがちょうどK個"""
    assert N >= 0
    if N < 10:
        if K == 0:
            return 1
        if K == 1:
            return N
        return 0
    (q, r) = divmod(N, 10)
    ret = 0
    if K >= 1:
        ret += F(q, K - 1) * r
        ret += F(q - 1, K - 1) * (9 - r)
    ret += F(q, K)
    return ret


print(F(N, K))
