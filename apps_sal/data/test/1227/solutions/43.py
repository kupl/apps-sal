import sys

from functools import lru_cache

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())


@lru_cache(None)
def F(N, K):
    """(0以上）N以下で、0でないものがちょうどK個"""

    assert N >= 0  # Nが非負であることを保証する

    if N < 10:  # N が一桁
        if K == 0:  # 使える 0 以外の数がない場合
            return 1  #
        if K == 1:
            return N  # 1,2,...,N までのどれか
        return 0  # それ以上 K が余っていたら作れない

    q, r = divmod(N, 10)  # N = 10*q + r と置く

    ret = 0
    if K >= 1:
        # 1の位(r)が nonzero
        ret += F(q, K - 1) * r  #
        ret += F(q - 1, K - 1) * (9 - r)

    # 1の位(r)が zero
    ret += F(q, K)
    return ret


print((F(N, K)))

