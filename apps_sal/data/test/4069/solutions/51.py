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
    X, K, D = input_to_int_map()

    temp = abs(X) // D

    if K < temp:
        return int(abs(X) - (K * D))

    if (K - temp) % 2 == 0:
        return int(abs(X) - (D * temp))

    return int(abs(abs(X) - (D * temp) - D))


def __starting_point():
    print((main()))

__starting_point()
