from collections import deque
from heapq import heappop, heappush
from random import randint
import time


def main():
    N = int(input())
    idx2 = 1
    while N - pow(5, idx2) >= 1:
        tmp = N - pow(5, idx2)
        idx = 1
        while tmp - pow(3, idx) >= 0:
            if tmp == pow(3, idx):
                print(idx, idx2)
                return 0
            else:
                idx += 1
        idx2 += 1
    print(-1)


def __starting_point():
    main()


__starting_point()
