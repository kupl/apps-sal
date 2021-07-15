# -*- coding: utf-8 -*-

# 入力を整数に変換して受け取る
def input_int():
    return int(input())


# マイナス1した値を返却
def int1(x):
    return int(x) - 1


# 半角スペース区切り入力をIntに変換してMapで受け取る
def input_to_int_map():
    return list(map(int, input().split()))


# 半角スペース区切り入力をIntに変換して受け取る
def input_to_int_tuple():
    return tuple(map(int, input().split()))


# 半角スペース区切り入力をIntに変換してマイナス1した値を受け取る
def input_to_int_tuple_minus1():
    return tuple(map(int1, input().split()))


def main():
    S = input_int()
    mod = 10 ** 9 + 7
    ans_list = [0] * 2001
    ans_list[0] = 0
    ans_list[1] = 0
    ans_list[2] = 0
    ans_list[3] = 1

    for i in range(4, S + 1):
        ans_list[i] = ans_list[i - 1] + ans_list[i - 3]
        ans_list[i] %= mod
    print((ans_list[S]))



def __starting_point():
    main()

__starting_point()
