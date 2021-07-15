def main():
    def calc_x_y(mi):
        """取り除いた要素の最小値がmiとなるように
        操作をQ回行えるか
        行える -> Q回の操作で取り除いた要素の最大値 - mi
        行えない -> -1
        """

        cont = 0
        removed = []
        for i, x in enumerate(a):
            if x < mi:
                if cont >= K:
                    removed += sorted(a[i - cont:i])[:cont - K + 1]
                cont = 0
                continue
            cont += 1
        else:
            if cont >= K:
                removed += sorted(a[-cont:])[:cont - K + 1]

        if len(removed) >= Q:
            removed.sort()
            return removed[Q - 1] - mi
        else:
            return -1

    N, K, Q = list(map(int, input().split()))
    *a, = list(map(int, input().split()))

    mi_cands = sorted(set(a))

    ans = 10 ** 9
    for mi in mi_cands:
        res = calc_x_y(mi)
        if ~res:
            ans = min(ans, res)

    print(ans)


def __starting_point():
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())

__starting_point()
