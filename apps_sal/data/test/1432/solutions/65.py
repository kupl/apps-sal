# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""


def main():
    N = int(input())
    A_lsit = list(map(int, input().split()))

    mount1_min = 0
    mount1_max = min(A_lsit[0], A_lsit[-1])

    mount_list = [0] * N

    while True:
        mount_list[0] = (mount1_min + mount1_max) // 2
        for i in range(N - 1):
            mount_list[i + 1] = A_lsit[i] - mount_list[i]
        # print(mount_list)
        if A_lsit[N - 1] - mount_list[N - 1] == mount_list[0]:
            break
        elif A_lsit[N - 1] - mount_list[N - 1] < mount_list[0]:
            mount1_max = mount_list[0]
        else:
            if mount1_min != mount_list[0]:
                mount1_min = mount_list[0]
            else:
                mount1_min = mount_list[0] + 1
    print((" ".join([str(m * 2) for m in mount_list])))


def __starting_point():
    main()


__starting_point()
