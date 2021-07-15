# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 23:10
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Yuhao and a Parenthesis.py


def calc_bracket(sequence):
    left_num, right_num = 0, 0
    for c in sequence:
        if c == ')':
            if left_num != 0:
                left_num -= 1
            else:
                right_num += 1
        else:
            left_num += 1
    return left_num, right_num


def main():
    total_num = int(input())

    result = 0
    left_dict, right_dict = {}, {}
    correct_num = 0

    for _ in range(total_num):
        sequence = input()
        left_num, right_num = calc_bracket(sequence)
        if left_num != 0 and right_num != 0:
            continue
        elif left_num:
            if right_dict.get(left_num, 0):
                right_dict[left_num] -= 1
                result += 1
            else:
                left_dict[left_num] = left_dict.get(left_num, 0) + 1
        elif right_num:
            if left_dict.get(right_num, 0):
                left_dict[right_num] -= 1
                result += 1
            else:
                right_dict[right_num] = right_dict.get(right_num, 0) + 1
        else:
            correct_num += 1

    result = result + correct_num // 2
    print(result)


def __starting_point():
    main()

__starting_point()
