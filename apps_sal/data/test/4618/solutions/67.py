# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S, K):
    n = len(S)
    l = [''] + ['あ'] * 5
    for i in range(n):
        for j in range(i, i + 5):
            tmp = S[i:j + 1]
            tmp_num = bisect.bisect_left(l, tmp)
            if tmp_num > 5:
                continue
            elif l[tmp_num] != tmp:
                l.insert(tmp_num, tmp)
                l.pop(-1)
    print((l[K]))


def __starting_point():
    S = input()
    K = int(input())
    solve(S, K)

    # # test
    # from random import randint
    # from func import random_str
    # n = 5000
    # S = random_str(n, 'abcde')
    # K = randint(1, 5)
    # print(S)
    # print(K)
    # solve(S, K)

__starting_point()
