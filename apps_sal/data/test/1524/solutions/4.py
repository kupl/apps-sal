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
    s = STR()
    ls = len(s)
    ans = [0] * ls
    flg = True
    ct = 0
    for i in range(ls):
        if flg:
            if s[i] == 'R':
                ct += 1
            else:
                ans[i] += ct // 2
                ans[i - 1] += ct // 2 + ct % 2
                ct = 1
                temp = i
                flg = False
        else:
            if s[i] == 'L':
                ct += 1
            else:
                ans[temp] += ct // 2 + ct % 2
                ans[temp - 1] += ct // 2
                ct = 1
                flg = True
    ans[temp] += ct // 2 + ct % 2
    ans[temp - 1] += ct // 2

    print(*ans)


def __starting_point():
    do()


__starting_point()
