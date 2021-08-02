#import math
#import itertools
#from collections import deque

INT = lambda: int(input())
INTM = lambda: map(int, input().split())
STRM = lambda: map(str, input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int, input().split()))
LISTS = lambda: list(map(str, input().split()))


def do():
    n, k = INTM()
    ans = 0
    for i in range(1, n + 1):
        temp = i
        ct = 0
        while temp < k:
            ct += 1
            temp *= 2
        ans += (1 / (n * (2**ct)))

    print(ans)


def __starting_point():
    do()


__starting_point()
