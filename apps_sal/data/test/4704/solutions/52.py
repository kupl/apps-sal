import os
import sys
from itertools import accumulate


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_ac = list(accumulate(A))
    ans = A_ac[-1]
    for (i, ac) in enumerate(A_ac):
        if i == 0:
            ans = abs(2 * ac - A_ac[-1])
        if i == N - 1:
            break
        if abs(2 * ac - A_ac[-1]) < ans:
            ans = abs(2 * ac - A_ac[-1])
    print(ans)


def __starting_point():
    main()


__starting_point()
