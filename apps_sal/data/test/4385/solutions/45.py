# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import numpy as np
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(a, b, c, d, e, k):
    arr = np.array([a, b, c, d, e])
    # print(arr)
    arr, arr2 = [a.flatten() for a in np.meshgrid(arr, arr)]
    # print(arr)
    arr = np.c_[arr, arr2]
    # print(arr)
    arr = np.array(list([abs(x[0] - x[1]) for x in arr]))
    # print(arr)
    print((':(' if arr.max() > k else 'Yay!'))


def __starting_point():
    a, b, c, d, e, k = [int(input()) for _ in range(6)]
    # print(a, b, c, d, e, k)
    solve(a, b, c, d, e, k)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
