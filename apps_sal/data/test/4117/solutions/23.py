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
    N = input_int()
    L = input_to_int_tuple()

    distinct_L = set(L)

    ret = 0
    if len(distinct_L) < 3:
        return ret

    # L = sorted(L)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                li, lj, lk = L[i], L[j], L[k]
                sorted_val = sorted([li, lj, lk])
                if sorted_val[0] != sorted_val[1] != sorted_val[2] and (sorted_val[0] + sorted_val[1]) > sorted_val[2]:
                    ret += 1

    return ret


def __starting_point():
    print((main()))

__starting_point()
