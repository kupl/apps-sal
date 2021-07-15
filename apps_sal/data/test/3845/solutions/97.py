# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B):
    ans = [['#' for _ in range(101)] for _ in range(101)]
    B -= 1
    for i in range(1, 101, 4):
        for j in range(1, 101, 4):
            if A + B == 0:
                break
            if A > 0 and B > 0:
                ans[i][j] = '.'
                ans[i][j + 1] = '.'
                ans[i][j + 2] = '.'
                ans[i + 1][j] = '.'
                ans[i + 1][j + 2] = '.'
                ans[i + 2][j] = '.'
                ans[i + 2][j + 1] = '.'
                ans[i + 2][j + 2] = '.'
                A -= 1
                B -= 1
            elif A > 0:
                ans[i][j] = '.'
                A -= 1
            elif B > 0:
                if j == 1:
                    ans[i - 1][j] = '.'
                    ans[i - 1][j + 1] = '.'
                    ans[i - 1][j + 2] = '.'
                ans[i][j - 1] = '.'
                ans[i + 1][j - 1] = '.'
                ans[i + 2][j - 1] = '.'
                ans[i][j] = '.'
                ans[i][j + 1] = '.'
                ans[i][j + 2] = '.'
                ans[i + 1][j] = '.'
                ans[i + 1][j + 2] = '.'
                ans[i + 2][j] = '.'
                ans[i + 2][j + 1] = '.'
                ans[i + 2][j + 2] = '.'
                B -= 1
        if A + B == 0:
            break

    print((100, 100))
    for anss in ans[1:]:
        print((''.join(anss[1:])))


def __starting_point():
    A, B = list(map(int, input().split()))
    solve(A, B)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()

__starting_point()
