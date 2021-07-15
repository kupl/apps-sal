# 解説を参考に作成
# 提出 #14841909 を参考に作成

# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N, As):
    import math
    x = 1 if max(As) == 0 else math.ceil(math.log2(max(As)))
    ans = 0
    mod = 10 ** 9 + 7

    for i in range(x):
        cnt = sum((A >> i) % 2 for A in As)
        ans += (cnt * (N - cnt)) * pow(2, i, mod)
        ans = ans % mod
    print(ans)


def __starting_point():
    N = int(input())
    As = [int(i) for i in input().split()]
    # N = 3 * 10 ** 5
    # import random
    # As = [random.randint(2 ** 59, 2 ** 60) for _ in range(N)]
    solve(N, As)

__starting_point()
