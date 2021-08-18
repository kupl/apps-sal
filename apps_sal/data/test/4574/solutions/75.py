

import os
import sys
from collections import Counter


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    a_cnt = [[key, val] for key, val in list(Counter(a).items()) if val >= 2]
    if len(a_cnt) == 0:
        print((0))
        return
    a_cnt.sort(key=lambda x: x[0], reverse=True)
    if a_cnt[0][1] >= 4:
        print((a_cnt[0][0]**2))
    elif len(a_cnt) == 1:
        print((0))
    else:
        print((a_cnt[0][0] * a_cnt[1][0]))


def __starting_point():
    main()


__starting_point()
