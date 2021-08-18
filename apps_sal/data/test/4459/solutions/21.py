

import os
import sys
from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_cnt = Counter(A)
    ans = 0
    for key, value in list(A_cnt.items()):
        if key == value:
            pass
        elif key > value:
            ans += value
        else:
            ans += value - key
    print(ans)


def __starting_point():
    main()


__starting_point()
