def ternary_search(*, l, r, func, loop_count=100, find_local_minimum: bool = True):
    """
    三分探索とは「たかだか一つしか極値のない関数fにおける極値を探索するアルゴリズム」
    https://qiita.com/ganariya/items/1553ff2bf8d6d7789127
    loop_count: 70-80で十分.厳密には2/3の冪乗で収束するか計算.epsで条件判定は無限ループが怖い.
    """

    if find_local_minimum:  # 極小値
        for i in range(loop_count):
            c1 = (l * 2 + r) / 3  # lr間を3等分した内分点
            c2 = (l + r * 2) / 3  # lr間を3等分した内分点
            if func(c1) > func(c2):
                l = c1  # 大きい方を(中央に)近づける
            else:
                r = c2
        return func(l)

    else:  # 極大値
        for i in range(loop_count):
            c1 = (l * 2 + r) / 3  # lr間を3等分した内分点
            c2 = (l + r * 2) / 3  # lr間を3等分した内分点
            if func(c1) < func(c2):
                l = c1  # 小さい方を(中央に)近づける
            else:
                r = c2
        return func(l)


def main():
    from collections import namedtuple
    from math import hypot
    import sys
    input = sys.stdin.readline

    MX = 1000

    Pt = namedtuple('Pt', 'x y')

    N = int(input())
    ps = [Pt(*list(map(int, input().split()))) for _ in range(N)]

    def max_dist(x, y):
        return max(hypot(x - p.x, y - p.y) for p in ps)

    def f(x):
        return ternary_search(
            l=0,
            r=MX + 1,
            func=lambda y: max_dist(x, y)
        )  # y[l,r),func=x,yを固定

    res = ternary_search(
        l=0,
        r=MX + 1,
        func=f
    )  # x[l,r),func=xを固定

    print(res)


def __starting_point():
    main()


__starting_point()
