# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
def lcm(a, b):
    """最小公倍数"""
    from math import gcd
    return (a * b) // gcd(a, b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, As):
    if sum([a % 2 for a in As]) > 0:
        print((0))
        return

    As = [a // 2 for a in As]
    all_lcm = 1
    for a in As:
        all_lcm = lcm(all_lcm, a)
        if all_lcm > M:
            print((0))
            return

    for a in As:
        if (all_lcm // a) % 2 == 0:
            print((0))
            return
    from math import ceil
    print((ceil(M // all_lcm / 2)))


def __starting_point():
    N, M = list(map(int, input().split()))
    As = [int(i) for i in input().split()]

    # import random
    # N, M = 10 ** 5, 10 ** 9
    # As = [random.randint(5, 5) * 2 for _ in range(N)]
    solve(N, M, As)


__starting_point()
