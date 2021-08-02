# coding:UTF-8
import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


def __starting_point():
    # ------ 入力 ------#
    # 1行入力
    aList = list(map(int, input().split()))     # スペース区切り連続数字

    x = 5

    # ------ 処理 ------#
    c5 = 0
    c7 = 0
    for a in aList:
        if a == 5:
            c5 += 1
        elif a == 7:
            c7 += 1

    # ------ 出力 ------#
    if c5 == 2 and c7 == 1:
        print("YES")
    else:
        print("NO")


__starting_point()
