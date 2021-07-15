# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 23:15
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : B1. Cat Party (Easy Edition).py

from collections import Counter


def check(counter, curr_len, curr_color, curr_one):
    if curr_len == 1 or curr_color == 1 or curr_one == curr_len:
        return True

    # if curr_len == 13:
    #     print(counter)
    if curr_one == 1:
        curr_color -= 1
    if (curr_len - 1) % curr_color != 0:
        return False
    correct_num = (curr_len - 1) // curr_color
    # if curr_len == 13:
    #     print(correct_num)

    false_count, false_num = 0, 0
    for i in range(1, 11):
        if counter[i] != correct_num and counter[i] != 0:
            false_count += 1
            false_num = counter[i]
    # if curr_len == 13:
    #     print(false_count)

    return false_count == 1 and (false_num - 1 == correct_num or false_count - 1 == 0)


def main():
    n = int(input())
    u = list(map(int, input().split()))

    counter = Counter()
    max_days, curr_color, curr_one = 0, 0, 0
    for i in range(n):
        if counter[u[i]] == 0:
            curr_color += 1
            curr_one += 1

        if counter[u[i]] == 1:
            curr_one -= 1

        counter[u[i]] += 1
        if check(counter, i + 1, curr_color, curr_one):
            max_days = i + 1
    print(max_days)


def __starting_point():
    main()

__starting_point()
