#import math
#import itertools
#from collections import deque

def INT(): return int(input())
def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())
def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


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
