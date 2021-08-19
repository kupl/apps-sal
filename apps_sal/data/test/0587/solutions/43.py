# 解説と下記を参考に作成
# https://atcoder.jp/contests/abc116/submissions/16781289
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, td):
    max_t = [0] * (N + 1)
    for i in range(N):
        if max_t[td[i][0]] < td[i][1]:
            max_t[td[i][0]], td[i][1] = td[i][1], max_t[td[i][0]]
    d = [tdi[1] for tdi in td]
    max_t.sort(reverse=True)
    d.sort(reverse=True)
    c_sum_max_t = [0]
    for i in range(N + 1):
        c_sum_max_t.append(c_sum_max_t[-1] + max_t[i])
    c_sum_d = [0]
    for i in range(N):
        c_sum_d.append(c_sum_d[-1] + d[i])
    ans = 0
    kind = len([i for i in max_t if i > 0])
    for i in range(1, min(kind + 1, K + 1)):
        # print(c_sum_max_t[i], c_sum_d[K - i], i ** 2, c_sum_max_t[i] + c_sum_d[K - i] + i ** 2)
        ans = max(c_sum_max_t[i] + c_sum_d[K - i] + i ** 2, ans)
    print(ans)
    # return ans


def __starting_point():
    N, K = list(map(int, input().split()))
    td = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, td)

    # # test
    # from random import randint
    # from func import random_str
    # import tmp
    # import copy
    #
    # while True:
    #     N, K = 10, randint(1, 10)
    #     td = [[randint(1, N), randint(2, 10 ** 2)] for _ in range(N)]
    #     my = solve(N, K, copy.deepcopy(td))
    #     ot = tmp.resolve(N, K, td)
    #     if my != ot:
    #         print(N, K)
    #         for tdi in td:
    #             print(tdi[0], tdi[1])
    #         print()
    #         print(my, ot)
    #         break


__starting_point()
