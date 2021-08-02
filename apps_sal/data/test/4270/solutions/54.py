#import math
#import itertools
#import numpy as np
import heapq
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#mod = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int, input().split())
STRM = lambda: map(str, input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int, input().split()))
LISTS = lambda: list(map(str, input().split()))


def do():
    n = INT()
    v = LIST()
    heapq.heapify(v)
    for i in range(n - 1):
        a = heapq.heappop(v)
        b = heapq.heappop(v)
        heapq.heappush(v, (a + b) / 2)
    print(heapq.heappop(v))


def __starting_point():
    do()


__starting_point()
