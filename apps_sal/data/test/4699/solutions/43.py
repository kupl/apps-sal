# coding:UTF-8
import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)

def __starting_point():
    # ------ 入力 ------#
    nk = list(map(int, input().split()))     # スペース区切り連続数字

    x = nk[1]
    dList = list(map(int, input().split()))     # スペース区切り連続数字

    # ------ 処理 ------#
    f = 0
    n = nk[0]
    while f == 0:
        nList = [int(c) for c in str(n)]  # 数字→単数字リスト変換
        b = 1
        for i in nList:
            for j in dList:
                if i == j:
                    b = 0
                    break
        if b == 1:
            break
        else:
            n += 1

    # ------ 出力 ------#
    print(("{}".format(n)))
    # if flg == 0:
    #     print("YES")
    # else:
    #     print("NO")

__starting_point()
