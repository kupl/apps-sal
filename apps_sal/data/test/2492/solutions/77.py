def binary_search(*, ok, ng, func):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    import sys
    import numpy as np
    inf = 10 ** 18 + 1
    input = sys.stdin.readline
    (N, K) = list(map(int, input().split()))
    A = np.array(input().split(), dtype=np.int64)
    A.sort()
    zero = A[A == 0]
    pos = A[A > 0]
    neg = A[A < 0]

    def count(x):
        """
        定数cに対して Ai*Aj<=c となる(i,j)の数え上げ
        順序制約 i<j -> 順序制約のない(i,j)からi==jの場合の個数を引いて2で割る
        iを固定して a=Ai とする
        a=0
            ax=0(<=c?),解なしまたは任意のx
        a>0
            ax<=c
            <-> x<=c/a
            <-> x<=c//a
        a<0
            ax<=c
            <-> (-a)x>=(-c)

            否定をとり,aの対候補全体=Nから引く

            (-a)x<(-c)
            <-> (-a)x<=(-c-1)
            <-> x<=(-c-1)//(-a)
        """
        cnt = 0
        if x >= 0:
            cnt += zero.size * N
        cnt += np.searchsorted(a=A, v=x // pos, side='right').sum()
        cnt += (N - np.searchsorted(a=A, v=(-x - 1) // -neg, side='right')).sum()
        cnt -= (A * A <= x).sum()
        assert cnt % 2 == 0
        return cnt // 2
    ans = binary_search(ng=-inf, ok=inf, func=lambda x: count(x) >= K)
    print(ans)


def __starting_point():
    main()


__starting_point()
