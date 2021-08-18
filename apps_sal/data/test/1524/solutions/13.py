

import os
import sys


def pivot_index(change_box, i, which):
    if which == 0:
        for cb in change_box:
            if cb >= i:
                return cb
    else:
        for j in range(len(change_box) - 1, -1, -1):
            if change_box[j] <= i:
                return change_box[j]


def main():
    S = input()
    change_box = []
    floor_chart = 1
    i = 0
    while i < len(S) - 1:
        if S[i] != S[i + 1] and floor_chart == 1:
            floor_chart = 0
            change_box.append(i)
        elif S[i] != S[i + 1] and floor_chart == 0:
            floor_chart = 1
        i += 1

    ans = [0] * len(S)
    one_cool = 0
    hash_one = 0
    for i in range(len(S)):
        if S[i] == 'R':
            if hash_one == 1:
                hash_one = 0
                one_cool += 1
            pidx = change_box[one_cool]
            cool = pidx - i
            if cool % 2 == 0:
                ans[pidx] += 1
            else:
                ans[pidx + 1] += 1

        else:
            pidx = change_box[one_cool] + 1
            hash_one = 1
            cool = i - pidx
            if cool % 2 == 0:
                ans[pidx] += 1
            else:
                ans[pidx - 1] += 1
    print(ans[0], end='')
    for i in range(1, len(ans)):
        print(" {}".format(ans[i]), end='')
    print()


def __starting_point():
    main()


__starting_point()
