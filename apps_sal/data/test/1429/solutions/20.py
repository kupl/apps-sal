
import sys
import io
import math
import collections
import decimal
import itertools
from queue import PriorityQueue
import bisect


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)


def solve(N, S):

    n = 0
    for i in range(-1, N - 1):
        count_a = 0
        count_g = 0
        count_c = 0
        count_t = 0
        for j in range(i + 1, N):
            if S[j] == 'A':
                count_a += 1
            elif S[j] == 'G':
                count_g += 1
            elif S[j] == 'C':
                count_c += 1
            elif S[j] == 'T':
                count_t += 1
            if (count_a == count_t) and (count_c == count_g):
                n += 1

    return n


def main():
    N, S = input().split()
    N = int(N)
    a = solve(N, S)
    print(a)


def __starting_point():
    main()


__starting_point()
