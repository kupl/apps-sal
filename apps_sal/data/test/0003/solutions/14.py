# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 13:43
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Painting the Fence.py


def main():
    n, q = list(map(int, input().split()))
    painters = []
    for _ in range(q):
        painters.append(list(map(int, input().split())))
    # print(painters)

    ret = 0
    for index in range(q):
        mask = [0] * (n + 1)
        for i in range(q):
            if i == index:
                continue
            left, right = painters[i]
            mask[left - 1] += 1
            mask[right] -= 1

        curr_sum, paint_count = 0, 0
        section_count = [0] * n
        for i in range(n):
            curr_sum += mask[i]
            section_count[i] = curr_sum
            if section_count[i] > 0:
                paint_count += 1

        one_count = [0] * (n + 1)
        for i in range(n):
            one_count[i + 1] = one_count[i] + (1 if section_count[i] == 1 else 0)

        desc_ones = n
        for i in range(q):
            if i == index:
                continue
            left, right = painters[i]
            desc_ones = min(desc_ones, one_count[right] - one_count[left - 1])

        ret = max(ret, paint_count - desc_ones)
    print(ret)


def __starting_point():
    main()


__starting_point()
