# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import math
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N):
    if N == 0:
        print('0')
        return
    x = math.ceil(math.log2(abs(N))) + 1
    minus = [(-2) ** i for i in range(1, x + 1, 2)]
    plus = [(-2) ** i for i in range(0, x + 1, 2)]
    minus.sort()
    plus.sort(reverse=True)

    minus_sum = [0]
    for m in minus:
        minus_sum.append(minus_sum[-1] + m)
    plus_sum = [0]
    for p in plus:
        plus_sum.append(plus_sum[-1] + p)

    ans = ''
    n = 0
    flg = True if len(plus) > len(minus) else False
    m = 0
    p = 0
    while True:
        if flg:
            tg = plus[p]
            p += 1
        else:
            tg = minus[m]
            m += 1

        if n + tg >= N:
            if n + tg != N and n + tg + (minus_sum[-1] - minus_sum[m]) > N:
                ans += '0'
            else:
                ans += '1'
                n += tg
        else:
            if n + tg + (plus_sum[-1] - plus_sum[p]) < N:
                ans += '0'
            else:
                ans += '1'
                n += tg
        flg = not flg
        if p >= len(plus) and m >= len(minus):
            break
    print((str(int(ans))))


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
