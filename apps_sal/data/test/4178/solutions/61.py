#import math
#import itertools
#import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#mod = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

def INT(): return int(input())
def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())
def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n = INT()
    h = LIST()
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            h[i + 1] -= 1
    flg = True
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            flg = False

    if flg:
        print('Yes')
    else:
        print('No')


def __starting_point():
    do()


__starting_point()
