#import math
#import itertools
#import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#MOD = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int, input().split())
STRM = lambda: map(str, input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int, input().split()))
LISTS = lambda: list(map(str, input().split()))


def do():
    n, k = INTM()
    A = LIST()
    suma = [0] * (n + 1)
    for i in range(n):
        suma[i + 1] = suma[i] + A[i]
    ans = 0
    for i in range(0, n + 1):
        low = i - 1
        high = n + 1
        check = suma[i] + k
        for j in range(20):
            mid = (low + high) // 2
            if suma[mid] < check:
                low = mid
            else:
                high = mid
        # print(low)
        ans += n - low
    # print(suma)
    print(ans)


def __starting_point():
    do()


__starting_point()
