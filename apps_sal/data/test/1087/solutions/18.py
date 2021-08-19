# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    import math
    max_K = 0
    for i in reversed(list(range(int(math.log2(K + 1)) + 1))):
        cnt = 0
        for a in A:
            if a >> i & 1:
                cnt += 1
        if cnt <= N // 2:
            if max_K + (1 << i) <= K:
                max_K += 1 << i
    ans = 0
    for a in A:
        ans += a ^ max_K
    print(ans)


def __starting_point():
    N, K = list(map(int, input().split()))
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
