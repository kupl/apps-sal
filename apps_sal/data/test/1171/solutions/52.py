# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
import heapq


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, Vi):
    ans = 0
    for ab in range(min(N, K) + 1):
        for a in range(ab + 1):
            b = ab - a
            have = Vi[:a] + Vi[N - b:]
            have.sort()
            s = sum(have)
            for i in range(K - ab):
                if len(have) <= i:
                    break
                elif have[i] < 0:
                    s += abs(have[i])
                else:
                    break
            ans = max(ans, s)
    print(ans)


def __starting_point():
    N, K = list(map(int, input().split()))
    Vi = [int(i) for i in input().split()]
    solve(N, K, Vi)

    # # test
    # import random
    # from func import random_str
    # N, K = 100, 50
    # Vi = [random.randint(-(10 ** 7), 10 ** 7) for _ in range(N)]
    # solve(N, K, Vi)

__starting_point()
