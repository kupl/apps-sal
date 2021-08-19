#!/usr/bin/env python3

import numpy as np


# def input():
#     return sys.stdin.readline().rstrip()


def main():
    n, k = list(map(int, input().split()))

    warps = list(map(int, input().split()))
    warps = [0] + warps
    # warps = np.array(warps, dtype=int)

    # order_num = np.zeros(len(warps) + 1, dtype=int)
    order_num = [0 for i in range(len(warps))]
    path_history = []

    node = 1
    while order_num[node] == 0:
        path_history.append(node)
        order_num[node] = len(path_history)
        node = warps[node]

    # print(order_num)
    # print(path_history)
    begin = order_num[node]
    # print(tail)

    if k <= begin:
        print((path_history[k]))
    else:
        # path_history = path_history[tail:]
        # print(path_history)
        leng = len(path_history) - order_num[node] + 1
        # print(leng)
        index = (k - (begin - 1)) % leng
        # print(index)
        print((path_history[begin - 1 + index]))


main()
