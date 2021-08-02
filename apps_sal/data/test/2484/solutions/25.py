#!/usr/bin python3
# -*- coding: utf-8 -*-

############################################
# しゃくとり法
############################################
# 区間において単調増加となるものの個数　ABC038_c
############################################

def main():
    N = int(input())
    A = list(map(int, input().split()))
##
    ret = 0
    right = 0
    tot = 0
    for left in range(0, N):
        while (right < N and ((tot ^ A[right] == tot + A[right]) or left == right)):  # 条件
            tot += A[right]
            right += 1
#        print(ret, left, right)
        ret += right - left  # 値の更新
        tot = tot ^ A[left]
    print(ret)


def __starting_point():
    main()


__starting_point()
