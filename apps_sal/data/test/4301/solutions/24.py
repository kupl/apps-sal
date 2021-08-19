import os
import sys
from collections import Counter


def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(int(input()))
    A_cnt = Counter(A)
    flag = 0
    A_max = max(A)
    A_next_max = sorted(A, reverse=True)[1]
    if A_cnt[A_max] > 1:
        flag = 1
    for a in A:
        if a == A_max and flag == 1:
            print(A_max)
        elif a == A_max and flag == 0:
            print(A_next_max)
        else:
            print(A_max)


def __starting_point():
    main()


__starting_point()
