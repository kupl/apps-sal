# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    dq = deque([(3, {3: 1, 5: 0, 7: 0}),
                (5, {3: 0, 5: 1, 7: 0}),
                (7, {3: 0, 5: 0, 7: 1})])
    ans = 0
    while dq:
        num, check = dq.popleft()
        if num > N:
            break
        if sum(check.values()) == 3:
            ans += 1
        for i in (3, 5, 7):
            new_num = num * 10 + i
            if new_num > N:
                break
            new_check = check.copy()
            new_check[i] = 1
            dq.append((new_num, new_check))
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
