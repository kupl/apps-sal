# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""


def main():
    N = int(input())
    S = input()

    solo_close_no = 0
    for i in range(N):
        if S[-i - 1] == ")":
            solo_close_no += 1
        elif solo_close_no >= 1:
            solo_close_no -= 1

    solo_open_no = 0
    for i in range(N):
        if S[i] == "(":
            solo_open_no += 1
        elif solo_open_no >= 1:
            solo_open_no -= 1

    answer = "(" * solo_close_no + S + ")" * solo_open_no
    print(answer)


def __starting_point():
    main()


__starting_point()
