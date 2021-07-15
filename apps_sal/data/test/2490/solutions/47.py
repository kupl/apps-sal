def main():
    *e, = list(map(int, input()))
    e.reverse()

    inf = 20 * len(e)

    dp = [0, inf]  # 繰り下がり無,有

    for x in e:
        ndp = [-1, -1]  # 繰り下がり無,有

        ndp[0] = min(
            dp[0] + x,
            dp[1] + ((x + 1) if x < 9 else inf)  # ちょうど支払えないのでinf
        )  # ちょうど支払う

        ndp[1] = min(
            dp[0] + ((10 - x) if x > 0 else inf),  # 繰り下がりにならないのでinf
            dp[1] + (10 - (x + 1))
        )  # 0枚支払って繰り下がり

        dp = ndp

    print((min(dp[0], dp[1] + 1)))


def __starting_point():
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok

__starting_point()
