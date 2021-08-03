import collections
import itertools
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()


def resolve():
    N, K = LI()
    xy = [LI() for _ in range(N)]

    # x, y全ての重複あり組み合わせに対して含まれる点の個数を算出する

    x_coord = [i[0] for i in xy]
    x_coord.sort()
    x_val_num = {x_coord[i]: i for i in range(N)}
    y_coord = [i[1] for i in xy]
    y_coord.sort()
    y_val_num = {y_coord[i]: i for i in range(N)}

    # 2次元累積和
    xy_cnt = [[0] * N for _ in range(N)]
    for x, y in xy:
        xy_cnt[y_val_num[y]][x_val_num[x]] = 1
    # for i in xy_cnt:
    #     print(i)
    xy_acm = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            xy_acm[i + 1][j + 1] = xy_cnt[i][j] + xy_acm[i + 1][j] + xy_acm[i][j + 1] - xy_acm[i][j]
    # for i in xy_acm:
    #     print(i)

    ans = INF
    for yl, yu in itertools.combinations(list(range(N + 1)), 2):
        for xl, xu in itertools.combinations(list(range(N + 1)), 2):
            cnt = xy_acm[yu][xu] - xy_acm[yu][xl] - xy_acm[yl][xu] + xy_acm[yl][xl]
            # print(cnt, yl, yu, xl, xu)
            if cnt >= K:
                ans = min((x_coord[xu - 1] - x_coord[xl]) * (y_coord[yu - 1] - y_coord[yl]), ans)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
