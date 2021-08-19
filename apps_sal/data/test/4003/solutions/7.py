"""Codeforces Round #555 (Div. 3)

Problem C. Increasing Subsequence

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""
__version__ = '1.0'
__date__ = '2019-04-26'
import sys


def rec_solve(a, l, r, last):
    choices = []
    while l <= r:
        if a[l] == a[r] and a[l] > last:
            sub_ans_1 = rec_solve(a, l + 1, r, a[l])
            sub_ans_2 = rec_solve(a, l, r - 1, a[l])
            if len(sub_ans_1) > len(sub_ans_2):
                choices.append('L')
                choices += sub_ans_1
                return choices
            else:
                choices.append('R')
                choices += sub_ans_2
                return choices
        elif a[l] < a[r] and a[l] > last:
            last = a[l]
            choices.append('L')
            l += 1
        elif a[r] > last:
            last = a[r]
            choices.append('R')
            r -= 1
        elif a[l] > last:
            last = a[l]
            choices.append('L')
            l += 1
        else:
            return choices
    return choices


def solve(n, a):
    return rec_solve(a, 0, n - 1, 0)


def main(argv=None):
    n = int(input())
    a = list(map(int, input().split()))
    choice = solve(n, a)
    print(len(choice))
    print(''.join(choice))
    return 0


def __starting_point():
    STATUS = main()
    return STATUS


__starting_point()
